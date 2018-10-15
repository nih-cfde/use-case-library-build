#!/usr/bin/env python
import os, re, sys
import subprocess
import oyaml as yaml
from collections import OrderedDict
#from nltk.stem import WordNetLemmatizer
from parse_input_files import parse_library_md

from utilities import scrub_overlap


"""
Extract Tags from YAML Header

This script extracts the YAML header from every 
markdown item in the use case library and creates
a tag list by extracting noun phrases.

Procedure:
    - For each markdown file
    - Extract the YAML header
    - Run each header string through noun phrase extractor
    - Process/filter tags/noun phrases
    - Add tags to YAML header
    - Update original markdown with new YAML header
"""

def usage():
    print("extract_header_tags.py:")
    print("This script iterates over each Markdown file with YAML headers,")
    print("extracts tags from the YAML header, and adds tags to the header.")
    print("")
    print("WARNING: This task will modify documents in-place.")
    print("")
    print("Usage:")
    print("    ./extract_header_tags.py [FLAGS] <path-to-markdown-files>")
    print("")
    print("        -n | --dry-run       Print the names of files that would be")
    print("                             changed if the script were run.")
    print("")
    print("Example:")
    print("    ./extract_header_tags.py ../library")
    print("")
    exit(1)

def main():

    if(len(sys.argv)<2):
        usage()

    # Extract dry run arguments, if present
    args = sys.argv[1:]
    dry_run = False
    for dry_run_flag in ['-n','--dry-run']:
        if(dry_run_flag in args):
            dry_run = True
            args.remove(dry_run_flag)

    # Set the location of the source files and check it exists
    SRC_DOCS = args[0]
    if not os.path.isdir(SRC_DOCS):
        err = "ERROR: No source directory %s was found."%(SRC_DOCS)
    
    # Walk the directory and look for Markdown files
    markdown_files = []
    for fdir,fdirnames,fnames in os.walk(SRC_DOCS):
        for f in fnames:

            # Check a set of conditions to see if we
            # really want to linkify this document.
            bool1 = f[-3:]=='.md'       # only add markdown
            bool2 = f[-7:]!='_new.md'   # ignore _new.md (?)
            bool3 = '.github' not in fdir  # ignore github templates

            if( bool1 and bool2 and bool3):
                markdown_files.append( os.path.join( fdir, f ) )


    ########################################
    # Strategy:
    # - Extract header
    # - Convert YAML to dict
    # - Extract tags from dictionary values
    # - Update YAML header
    # - Output to file
    ########################################



    # ------------------------------
    # We wait to do this until we get here,
    # so that we aren't wasting time importing
    # things we don't need.
    from np_extractor import NounPhraseExtractor
    # ------------------------------



    # For each markdown doc
    for kk, md in enumerate(markdown_files):
    
        print("-"*40,file=sys.stderr)
        print("Extracting YAML header tags from document: %s"%(md),file=sys.stderr)

        if dry_run is False:

            yaml_header, body = parse_library_md(md)

            # Step 1: compile the sentences where tags come from
            sentences = []
            for key in yaml_header:
                if key in ['title','blurb','input','output']:
                    value = yaml_header[key]
                    if type(value)==type(""):
                        sentences.append(value)

            # Step 2: extract noun phrases
            tags = []
            for sentence in sentences:
                np_extractor = NounPhraseExtractor(sentence)
                tags += np_extractor.extract()

            # Step 3: clean up tags (lowercase, remove dupes, remove overlap)
            tags = [tag.lower() for tag in tags]
            tags = list(set(tags))
            tags = scrub_overlap(tags)

            #lemma = WordNetLemmatizer()
            yaml_header['tags'] = tags

            head = yaml.dump(yaml_header, default_flow_style=False)
            head = re.sub('\n  ',' ',head)

            delim = '---\n'

            # write to target file
            with open(md,'w') as f:
                f.write(delim)
                f.write(head)
                f.write(delim)
                f.write(body)

            print("Finished extracting header tags from document: %s"%(md),file=sys.stderr)
            print("Extracted tags: %s"%( ", ".join(tags) ))

        else:

            print("Dry run would have extracted header tags from document: %s"%(md),file=sys.stderr)


if __name__=="__main__":
    main()


#!/usr/bin/env python
import os, re, sys
import subprocess
import oyaml as yaml
from textblob import TextBlob
from collections import OrderedDict

from parse_input_files import parse_library_md

from utilities import scrub_overlap, walk_dir_get_md_files


TEXTBLOB_IGNORE = 'textblob_ignore.dat'
TEXTBLOB_REPLACE = 'textblob_abbreviations.dat'

"""
Extract Tags from YAML Header

This script extracts the YAML header from every 
markdown item in the use case library and creates
a tag list by extracting noun phrases using textblob.

Procedure:
    - For each markdown file
    - Extract the YAML header
    - Run each header string through noun phrase extractor
    - Process/filter tags/noun phrases
    - Add tags to YAML header
    - Update original markdown with new YAML header
"""

def usage():
    print("extract_header_tags_textblob.py:")
    print("This script iterates over each Markdown file with YAML headers,")
    print("extracts tags from the YAML header, and adds tags to the header.")
    print("")
    print("WARNING: This task will modify documents in-place.")
    print("")
    print("Usage:")
    print("    ./extract_header_tags_textblob.py [FLAGS] <path-to-markdown-files>")
    print("")
    print("        -n | --dry-run       Print the names of files that would be")
    print("                             changed if the script were run.")
    print("")
    print("        -f | --force         If an item in the use case library already")
    print("                             contains tags, force overwrite the tags.")
    print("")
    print("        -s | --safe          If an item in the use case library already")
    print("                             contains tags, be safe and don't overwrite the tags.")
    print("")
    print("Example:")
    print("    ./extract_header_tags_textblob.py ../library")
    print("")
    exit(1)



def main():

    if(len(sys.argv)<2):
        usage()

    # Extract dry run argument, if present
    args = sys.argv[1:]
    dry_run = False
    for dry_run_flag in ['-n','--dry-run']:
        if(dry_run_flag in args):
            dry_run = True
            args.remove(dry_run_flag)

    # Extract force argument, if present
    args = sys.argv[1:]
    force_run = False
    for force_run_flag in ['-f','--force']:
        if(force_run_flag in args):
            force_run = True
            args.remove(force_run_flag)

    # Extract safe argument, if present
    args = sys.argv[1:]
    safe_run = False
    for safe_run_flag in ['-s','--safe']:
        if(safe_run_flag in args):
            safe_run = True
            args.remove(safe_run_flag)

    if safe_run and force_run:
        err = "ERROR: Cannot do safe run and force run together. Specify one of -f or -s."
        raise Exception(err)

    # Set the location of the source files and check it exists
    SRC_DOCS = args[0]
    if not os.path.isdir(SRC_DOCS):
        err = "ERROR: No source directory %s was found."%(SRC_DOCS)
        raise Exception(err)
    
    markdown_files = walk_dir_get_md_files(SRC_DOCS)

    ########################################
    # Strategy:
    # - Extract header
    # - Convert YAML to dict
    # - Extract tags from dictionary values
    # - Update YAML header
    # - Output to file
    ########################################

    # For each markdown doc
    for kk, md in enumerate(markdown_files):
    
        print("-"*40,file=sys.stderr)
        print("Extracting YAML header tags from document: %s"%(md),file=sys.stderr)

        if dry_run is False:

            yaml_header, body = parse_library_md(md)

            if 'tags' not in yaml_header.keys() or force_run:

                # No tags yet, so populate tags wtih automatically extracted tags

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
                    blob = TextBlob(sentence)
                    tags += [str(j) for j in blob.noun_phrases]

                # Step 3: clean up tags (case, remove dupes, remove overlap)
                tags = fix_replace(tags)
                tags = list(set(tags))
                tags = scrub_overlap(tags)

                # Step 4: remove tags we are ignoring
                with open(TEXTBLOB_IGNORE,'r') as f:
                    ignore_tags = [line.strip() for line in f.readlines() if line[0] != '#']
                tags = [j for j in tags if j not in ignore_tags]

                # Step 5: sort tags
                tags = sorted(tags)

                if len(tags)>0:
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
                print("Document already contains tags: %s"%(md),file=sys.stderr)

        else:

            print("Dry run would have extracted header tags from document: %s"%(md),file=sys.stderr)


def fix_replace(tags):
    """
    Perform replacement of phrases using the 
    list in the replace file.
    """
    with open(TEXTBLOB_REPLACE,'r') as f:
        lines = [line.strip() for line in f.readlines()]

    case_fixes = {}
    for line in lines:
        (k,v) = line.split(":")
        k = k.strip()
        v = v.strip()
        case_fixes[k] = v

    new_tags = []
    for tag in tags:

        new_tag = tag

        for case_fix in case_fixes.keys():
            if case_fix in new_tag:
                r = case_fix
                s = case_fixes[r]
                new_tag = re.sub(r,s,new_tag)

        new_tags.append(new_tag)

    return new_tags


if __name__=="__main__":
    main()


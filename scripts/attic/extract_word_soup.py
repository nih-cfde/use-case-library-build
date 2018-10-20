#!/usr/bin/env python
import os, re, sys
import subprocess
import oyaml as yaml
from collections import OrderedDict
from parse_input_files import parse_library_md

WORD_SOUP_FILE = 'word_soup.txt'

with open('stop_words.txt','r') as f:
    STOP_WORD_LIST = f.readlines()
STOP_WORD_LIST = [word.strip() for word in STOP_WORD_LIST]


"""
Extract Word Soup
Markdown + YAML Headers


This script iterates over every Markdown file in the
library and performs the following set of operations:

- remove the YAML header
- extract words from the YAML header strings (into word_soup.txt)
- pass the body through Pandoc Github-flavored markdown to JSON
- apply a panflute filter to extract words from paragraphs (into word_soup.txt)
- pass the body back through Pandoc JSON to Github-flavored markdown
- re-attach the YAML header
- dump the header + body into the original Markdown file

The end result is word_soup.txt, which can be used to generate
a list of most common words, which will lead to a pool of tags.
"""

def usage():
    print("extract_word_soup.py:")
    print("This script iterates over each Markdown file with YAML headers,")
    print("linkifies the body, and extracts a word soup from the header and")
    print("body for the purposes of building a tag list.")
    print("")
    print("WARNING: This task will modify documents in-place.")
    print("")
    print("Usage:")
    print("    ./extract_word_soup.py [FLAGS] <path-to-markdown-files>")
    print("")
    print("        -n | --dry-run       Print the names of files that would be")
    print("                             changed if the script were run.")
    print("")
    print("Example:")
    print("    ./extract_word_soup.py ../library")
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
    # Extract word soup strategy for Markdown + YAML:
    # - tear off yaml header
    # - extract word soup from yaml header
    # - store body in temp file
    # - apply pandoc gfm to json with temp file
    # - apply panflute filter to extract word soup from body
    # - apply pandoc json to gfm
    # - paste YAML header back on
    # - output to file
    ########################################

    if os.path.exists(WORD_SOUP_FILE):
        print("Word soup file %s alreeady exists, removing it."%(WORD_SOUP_FILE))
        os.remove(WORD_SOUP_FILE)


    # Extract word soup from each document
    for kk, md in enumerate(markdown_files):
    
        print("-"*40,file=sys.stderr)
        print("Extracting word soup from document: %s"%(md),file=sys.stderr)

        if dry_run is False:

            yaml_header, body = parse_library_md(md)

            # make a new backup file
            backup_md = re.sub('.md$','.md.secondary',md)

            with open(backup_md,'w') as f:
                f.write(body)

            # cat md (we will pass this to pandoc)
            cat_cmd = ['cat', backup_md]
            cat_proc = subprocess.Popen(cat_cmd,
                    stdout=subprocess.PIPE)

            # pandoc: md to json
            pandoc_from_cmd = ['pandoc','-f','gfm','-t','json','-s']
            pandoc_from_proc = subprocess.Popen(pandoc_from_cmd, 
                    stdin=cat_proc.stdout,
                    stdout=subprocess.PIPE)


            ##########################
            # Extract word soup from the
            # YAML header components,
            # and add them to the
            # word soup.

            for key in yaml_header:
                value = yaml_header[key]
                if type(value)==type(""):
                    soup = value.split(" ")
                    soup = [re.sub(r'\.$','',w) for w in soup]
                    soup = [w.lower() for w in soup]
                    soup = [w for w in soup if w not in STOP_WORD_LIST]
                    with open(WORD_SOUP_FILE,'a') as f:
                        f.write("\n".join(soup))
                        f.write("\n")

            ##########################
            # Apply a custom panflute filter:
            # 
            # Walk the document and extract 
            # word soup from the paragraphs

            FILTER = os.path.join(os.getcwd(),'filter_word_soup.py')

            # filter: json to json
            pandoc_filter_cmd = [FILTER]
            pandoc_filter_proc = subprocess.Popen(pandoc_filter_cmd, 
                    stdin=pandoc_from_proc.stdout,
                    stdout=subprocess.PIPE)
            
            # pandoc: json to markdown
            pandoc_to_cmd = ['pandoc','-f','json','-t','gfm']
            pandoc_to_proc = subprocess.Popen(pandoc_to_cmd, 
                    stdin=pandoc_filter_proc.stdout,
                    stdout=subprocess.PIPE)

            # we now have the text of the pandoc output
            pandoc_output = pandoc_to_proc.stdout.read().decode('utf-8')

            # apply any regex filtering at this point
            # 
            # github checkboxes (not handled well by pandoc...)
            # \[x\] or \[X\] into [x]
            pandoc_output = re.sub(r'\\\[X\\\]','[x]',pandoc_output)
            pandoc_output = re.sub(r'\\\[x\\\]','[x]',pandoc_output)
            pandoc_output = re.sub(r'\\\[ \\\]','[ ]',pandoc_output)
            pandoc_output = re.sub(r'\\\[\\\]', '[ ]',pandoc_output)
            final_document = pandoc_output

            # -------------------------------------
            # target file is same as source/input file
            target = md

            delim = '---\n'

            head = yaml.dump(yaml_header, default_flow_style=False)
            head = re.sub('\n  ',' ',head)


            # write to target file
            with open(target,'w') as f:
                f.write(delim)
                f.write(head)
                f.write(delim)
                f.write(body)

            # remove backup file
            os.remove(backup_md)

            print("Finished extracting word soup from document: %s"%(target),file=sys.stderr)

        else:

            # target file is same as source/input file
            target = md

            print("Dry run would have extracted word soup from document: %s"%(target),file=sys.stderr)


if __name__=="__main__":
    main()


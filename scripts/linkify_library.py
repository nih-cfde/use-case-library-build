#!/usr/bin/env python
import os, re, sys
import subprocess
import oyaml as yaml
from collections import OrderedDict

from parse_input_files import parse_library_md

from utilities import \
        walk_dir_get_md_files, subdir, \
        GITHUB_LIBRARY_LOCATION, GITHUB_EDIT_LOCATION

"""
Linkify Use Case Library
Markdown + YAML Headers


This script iterates over every Markdown file in the
library and performs the following set of operations:

- remove the YAML header
- pass the body through Pandoc Github-flavored markdown to JSON
- pass the body back through Pandoc JSON to Github-flavored markdown (linkify)
- re-attach the YAML header
- dump the header + body into the original Markdown file
"""

def usage():
    print("linkify_library.py:")
    print("This script iterates over each Markdown file with YAML headers,")
    print("removes the YAML header, linkifies the body with pandoc, and")
    print("re-attaches the YAML header.")
    print("")
    print("WARNING: This task will modify documents in-place.")
    print("")
    print("Usage:")
    print("    ./linkify_library.py [FLAGS] <path-to-markdown-files>")
    print("")
    print("        -n | --dry-run       Print the names of files that would be")
    print("                             changed if the script were run.")
    print("")
    print("Example:")
    print("    ./linkify_library.py ../library")
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
    
    # Get all markdown files in library
    markdown_files = walk_dir_get_md_files(SRC_DOCS)

    ########################################
    # Linkify strategy for Markdown + YAML:
    # - tear off yaml header
    # - store body in temp file
    # - apply pandoc gfm to json with temp file
    # - apply pandoc json to gfm
    # - paste YAML header back on
    # - output to file
    ########################################

    # For each markdown doc
    for kk, md in enumerate(markdown_files):
    
        print("-"*40,file=sys.stderr)
        print("Linkifying (in-place) document: %s"%(md),file=sys.stderr)

        if dry_run is False:

            yaml_header, body = parse_library_md(md)

            # make a new backup file
            backup_md = re.sub('.md$','.md.secondary',md)

            with open(backup_md,'w') as f:
                f.write("\n".join(body))

            # cat md (we will pass this to pandoc)
            cat_cmd = ['cat', backup_md]
            cat_proc = subprocess.Popen(cat_cmd,
                    stdout=subprocess.PIPE)

            # pandoc: md to json
            pandoc_from_cmd = ['pandoc','-f','gfm','-t','json','-s']
            pandoc_from_proc = subprocess.Popen(pandoc_from_cmd, 
                    stdin=cat_proc.stdout,
                    stdout=subprocess.PIPE)

            # pandoc: json to md
            pandoc_to_cmd = ['pandoc','-f','json','-t','gfm']
            pandoc_to_proc = subprocess.Popen(pandoc_to_cmd, 
                    stdin=pandoc_from_proc.stdout,
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

            print("Finished linkifying document: %s"%(target),file=sys.stderr)

        else:

            # target file is same as source/input file
            target = md

            print("Dry run would have linkified document: %s"%(target),file=sys.stderr)


if __name__=="__main__":
    main()


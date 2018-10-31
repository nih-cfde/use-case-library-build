#! /usr/bin/env python
import sys
import argparse
import os
import shutil
import traceback

from jinja2 import Environment, FileSystemLoader

from utilities import \
        walk_dir_get_md_files, subdir, \
        md_files_to_obj_dict, \
        check_library_refs, resolve_library_refs, \
        GITHUB_LIBRARY_LOCATION, GITHUB_EDIT_LOCATION


"""
Rewrite (Repair) Files in the Use Case Library

This script rewrites files in the use case library 
under the library/ folder in a way that improves
and fixes problems.

This script does the following:
- Set up and validate reference structure between library items
- Use Jinja tempates (see templates dir) to build markdown output files
- Creates an mkdocs.yml configuration
"""

GITHUB_LIBRARY_LOCATION="https://github.com/dcppc/use-case-library/tree/master/library/"
GITHUB_EDIT_LOCATION="https://github.com/dcppc/use-case-library/edit/master/library/"

basepath = os.path.join(os.path.dirname(__file__), '..')
basepath = os.path.abspath(basepath)

def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('library_dir')
    args = p.parse_args(argv)

    # Get all markdown files in library
    markdown_files = walk_dir_get_md_files(args.library_dir)

    print('Found {} input files under library/'.format(len(inputfiles)))

    # Load each library file into obj_dict
    obj_dict = md_files_to_obj_dict(markdown_files)

    # Load each library file into obj_dict
    obj_dict = md_files_to_obj_dict(markdown_files)

    print('Loaded {} objects'.format(len(obj_dict)))

    print('Resolving references')
    obj_dict = resolve_library_refs(obj_dict)

    print('Checking references')
    check_library_refs(obj_dict)


    # Unique portion of this script:

    #
    # re-write each file in the library.
    # as it is, this script will strip \n 
    # off the end of the file.
    #

    for filename in inputfiles:
        with open(filename, 'rt') as fp:
            lines = list(fp)
            lines = [ x.rstrip("\n") for x in lines ]

    return 0

if __name__ == '__main__':
    sys.exit(main())

#! /usr/bin/env python
import sys
import argparse
import os
import shutil
import traceback

from jinja2 import Environment, FileSystemLoader

from utilities import \
        walk_dir_get_md_files, subdir, \
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

    print('found {} input files under library/'.format(len(inputfiles)))

    #
    # second, load all of the library files => obj_dict
    #

    obj_dict = {}
    for filename in inputfiles:
        # load markdown file + header
        header, content = parse_input_files.parse_library_md(filename)

        # create library object according to filename & header
        obj = create_library_object(filename, header, content)
        if obj.ident in obj_dict:
            raise Exception("duplicate identity: " + obj.ident)

        obj_dict[obj.ident] = obj

    print('loaded {} objects'.format(len(obj_dict)))

    print('resolving references')
    for obj in obj_dict.values():
        obj.resolve_references(obj_dict)

    print('checking references')
    for obj in obj_dict.values():
        if obj.obj_type == 'EPIC' and not obj.narrative:
            print('WARNING, orphaned epic {} has no parent narrative!'.format(obj.ident))

    for filename in inputfiles:
        with open(filename, 'rt') as fp:
            lines = list(fp)
            lines = [ x.rstrip("\n") for x in lines ]

    return 0

if __name__ == '__main__':
    sys.exit(main())

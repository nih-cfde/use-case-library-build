#! /usr/bin/env python
"""
Process the use case library files under library/ and create a mkdocs site.

This script does a bunch of things:
* sets up & validates a references structure between the files in library/
* uses jinja2 templates under templates/ to build markdown output files
* creates a mkdocs.yml configuration.
"""
import sys
import argparse
import os
import shutil
import traceback

GITHUB_LIBRARY_LOCATION="https://github.com/dcppc/use-case-library/tree/master/library/"
GITHUB_EDIT_LOCATION="https://github.com/dcppc/use-case-library/edit/master/library/"

from jinja2 import Environment, FileSystemLoader

from library_objects import create_library_object
import parse_input_files

basepath = os.path.join(os.path.dirname(__file__), '..')
basepath = os.path.abspath(basepath)

def subdir(location):
    return os.path.join(basepath, location)

def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('library_dir')
    args = p.parse_args(argv)

    inputfiles = set()
    for root, dirs, files in os.walk(args.library_dir):
        for name in files:
            if name.endswith('.md'):
                inputfiles.add(os.path.join(root, name))

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
        if hasattr(obj, 'blurb'):
            if not obj.blurb.endswith('.'):
                print('WARNING, blurb for {} does not end with a period.'.format(obj.ident))

    for filename in inputfiles:
        with open(filename, 'rt') as fp:
            lines = list(fp)
            lines = [ x.rstrip("\n") for x in lines ]

        new_lines = []
        for x in lines:
            if x.startswith('blurb:') and not x.endswith('.'):
                x += '.'
            new_lines.append(x)

        with open(filename + '.fix', 'wt') as fp:
            fp.write("\n".join(new_lines))
            fp.write("\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())

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

    jinja_env = Environment(
        loader=FileSystemLoader(subdir('templates'))
    )

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

    #
    # create output locations. Note, 'output/docs' is completely recreated
    # each time.
    #

    try:
        shutil.rmtree(subdir('output/docs'))
    except FileNotFoundError:
        pass

    try:
        os.mkdir(subdir('output'))
    except FileExistsError:
        pass
    os.mkdir(subdir('output/docs'))

    #
    # define a few utility functions for templates
    #

    def yield_objects(obj_type):
        x = []
        for obj in obj_dict.values():
            if obj.obj_type == obj_type:
                ot, number = obj.ident.split('-')
                number = int(number)
                x.append((number, ot, obj))

        return [ obj for _, _, obj in sorted(x) ]

    def make_title_link(obj):
        if obj is None:
            raise ValueError("null object passed in to make_title_link!")
        return "[{}]({})".format(obj.title, obj.ident + '.md')

    def make_view_link(obj, link_text):
        if obj is None:
            raise ValueError("null object passed in to make_edit_link!")
        return "[{}]({})".format(link_text,
                                 GITHUB_LIBRARY_LOCATION + obj.filename)

    def make_edit_link(obj, link_text):
        if obj is None:
            raise ValueError("null object passed in to make_edit_link!")
        return "[{}]({})".format(link_text,
                                 GITHUB_EDIT_LOCATION + obj.filename)

    # function to render a specific template
    count = 0
    def render_template(filename, outpath=None, **kw):
        nonlocal count
        if not outpath:
            outpath = os.path.join(subdir('output/docs'), filename)

        input_names = dict(yield_objects=yield_objects,
                           make_title_link=make_title_link,
                           make_view_link=make_view_link,
                           make_edit_link=make_edit_link,
                           len=len)
        input_names.update(kw)

        try:
            template = jinja_env.get_template(filename)
        except:
            traceback.print_exc()
            print('on template:', filename)
            return False

        print('\rcreating:', outpath, end='')

        try:
            rendered = template.render(input_names)
        except:
            traceback.print_exc()
            print('on file:', filename)
            return False
        
        with open(outpath, 'wt') as fp:
            fp.write(rendered)

        count += 1

        return True

    #
    # render all the things!
    #

    render_template('index.md')
    render_template('CONTRIBUTING.md')
    render_template('use-case-template.md')
    render_template('full_list.md')
    render_template('glossary.md')
    render_template('mkdocs.yml', subdir('output/mkdocs.yml'))

    for obj in obj_dict.values():
        filename = os.path.join(subdir('output/docs'), obj.ident + '.md')

        if not render_template(obj.template, filename, obj=obj):
            print('\nFAILED on', filename)
            return 1

    print(u'\r\033[K', end='')
    print('\rcreated {} pages total'.format(count))

    return 0

if __name__ == '__main__':
    sys.exit(main())

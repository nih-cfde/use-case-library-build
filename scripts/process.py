#! /usr/bin/env python
import sys
import argparse
import os
import shutil
import traceback

from jinja2 import Environment, FileSystemLoader

from utilities import walk_dir_get_md_files, subdir


"""
Process the Use Case Library

This script processes the use case library files
under the library/ folder and uses them to create
the mkdocs use case library site.

This script does the following:
- Set up and validate reference structure between library items
- Use Jinja tempates (see templates dir) to build markdown output files
- Creates an mkdocs.yml configuration
"""

def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('library_dir')
    args = p.parse_args(argv)

    # Load jinja templates from disk (templates folder)
    jinja_env = Environment(
        loader=FileSystemLoader(subdir('templates'))
    )

    # Get all markdown files in library
    markdown_files = walk_dir_get_md_files(args.library_dir)

    print('Found {} input files in library/'.format(len(markdown_files)))

    # Load each library file into obj_dict
    obj_dict = md_files_to_obj_dict(markdown_files)


    print('Loaded {} objects'.format(len(obj_dict)))

    print('Resolving references')
    obj_dict = resolve_library_refs(obj_dict)

    print('Checking references')
    for obj in obj_dict.values():
        if obj.obj_type == 'EPIC' and not obj.narrative:
            print('WARNING: orphaned epic {} has no parent narrative!'.format(obj.ident))

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

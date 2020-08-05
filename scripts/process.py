#! /usr/bin/env python
import sys
import argparse
import os
import re
import shutil
import traceback

from jinja2 import Environment, FileSystemLoader

from utilities import \
        walk_dir_get_md_files, subdir, \
        md_files_to_obj_dict, \
        check_library_refs, resolve_library_refs, \
        GITHUB_LIBRARY_LOCATION, GITHUB_EDIT_LOCATION

ABBREVIATIONS_REPLACE = 'textblob_abbreviations.dat'

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
    check_library_refs(obj_dict)


    # Unique portion of this script:

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
    # abbreviations (useful)
    # 

    abf = os.path.join(os.path.dirname(os.path.realpath(__file__)),ABBREVIATIONS_REPLACE)
    with open(abf,'r') as f:
        lines = [line.strip() for line in f.readlines()]

    case_fixes = {}
    for line in lines:
        (k,v) = line.split(":")
        k = k.strip()
        v = v.strip()
        case_fixes[k] = v


    #
    # define a few utility functions for templates
    #

    def yield_objects(obj_type):
        x = []
        for obj in obj_dict.values():
            if obj.obj_type == obj_type:
                assert '-' in obj.ident, "identifiers must have - in them"
                ot, number = obj.ident.split('-')
                number = int(number)
                x.append((number, ot, obj))

        return [ obj for _, _, obj in sorted(x) ]

    def make_first_lowercase(s):
        if s is None:
            raise ValueError("null object passed in to make_firstchar_lowercase()!")
        # Need to check for abbreviations here
        # ^pattern
        new_s = s[0].lower() + s[1:]
        for case_fix in case_fixes:
            k = case_fix
            v = case_fixes[k]

            s_lower = s.lower()
            if re.match(k,s_lower):
                find_this = r'^%s'%(k)
                replace_with_this = r'%s'%(v)
                new_s = re.sub(find_this, replace_with_this, new_s, flags=re.IGNORECASE)

        return new_s

    def make_title_link(obj):
        if obj is None:
            raise ValueError("null object passed in to make_title_link()!")
        return "[{}]({})".format(obj.title, obj.ident + '.md')

    def make_view_link(obj, link_text):
        if obj is None:
            raise ValueError("null object passed in to make_edit_link()!")
        return "[{}]({})".format(link_text,
                                 GITHUB_LIBRARY_LOCATION + obj.filename)

    def make_edit_link(obj, link_text):
        if obj is None:
            raise ValueError("null object passed in to make_edit_link()!")
        return "[{}]({})".format(link_text,
                                 GITHUB_EDIT_LOCATION + obj.filename)

    # function to render a specific template
    count = 0
    def render_template(filename, outpath=None, **kw):
        nonlocal count
        if not outpath:
            outpath = os.path.join(subdir('output/docs'), filename)

        input_names = dict(yield_objects=yield_objects,
                make_first_lowercase=make_first_lowercase,
                make_title_link=make_title_link,
                make_view_link=make_view_link,
                make_edit_link=make_edit_link,
                case_fixes=case_fixes,
                len=len)
        input_names.update(kw)

        try:
            template = jinja_env.get_template(filename)
        except:
            traceback.print_exc()
            print(' in template:', filename)
            return False

        print('\rcreating:', outpath, end='')

        try:
            rendered = template.render(input_names)
        except:
            traceback.print_exc()
            print(' in file:', filename)
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
    render_template('LICENSE.md')
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

import sys
import os
from library_objects import create_library_object
import parse_input_files

"""
Utilities

This file defines utilities useful for *all*
the use case library scripts in this directory.
"""

GITHUB_LIBRARY_LOCATION="https://github.com/dcppc/use-case-library/tree/master/library/"
GITHUB_EDIT_LOCATION="https://github.com/dcppc/use-case-library/edit/master/library/"


def check_library_refs(obj_dict):
    """
    Check library items to ensure they have all the links
    to other library items that they ought to.
    """
    warnings = []
    fail = False
    for obj in obj_dict.values():

        # User stories that aren't called from any epics
        if obj.obj_type == 'USE CASE':
            uc_reqs = obj.requirements
            task_reqs = []
            for t in obj.user_tasks:
                task_reqs.extend(t.requirements)

            uc_reqs = set([ r.ident for r in uc_reqs ])
            task_reqs = set([ r.ident for r in task_reqs ])
            if task_reqs != uc_reqs:
                remainder = task_reqs ^ uc_reqs
                idents = ", ".join(remainder)
                warn = f"ERROR: use case has disjoint requirements with its tasks' requirements for {obj.ident}! Check these requirements: {idents}"
                warnings.append(warn)
                fail = True


    warnings = sorted(warnings)
    for warning in warnings:
        print(warning)

    if fail:
        print('one or more errors are actually fatal. dying now.')
        sys.exit(-1)


def resolve_library_refs(obj_dict):
    """
    For each library item,
    resolve the references
    to other library items
    in the object dictionary.
    """
    for obj in obj_dict.values():
        obj.resolve_references(obj_dict)

    return obj_dict

def get_basepath(f):
    """
    Get the directory one dir level up from f
    """
    a = os.path.abspath(f)
    d = os.path.dirname(a)
    b = os.path.join(d,'..')
    c = os.path.abspath(b)
    return c

def subdir(location):
    basepath = get_basepath(__file__)
    return os.path.join(basepath, location)

def scrub_overlap(tags):
    """
    For a given list of tags, find tags that overlap
    with other tags. When overlapping tags are found,
    only keep the longer of the two tags.
    """
    del_ix = []
    ntags = len(tags)
    for i in range(0,ntags):
        for j in range(i+1,ntags):

            if tags[i] in tags[j]:
                del_ix.append(i)

            if tags[j] in tags[i]:
                del_ix.append(j)

    tags = [j for i,j in enumerate(tags) if i not in del_ix]
    return tags


def walk_dir_get_md_files(mypath):
    """
    Recursively walk the directory mypath and compile
    a list of all Markdown files found.
    Return the list of Markdown files.
    """
    markdown_files = []
    for fdir,fdirnames,fnames in os.walk(mypath):
        for f in fnames:
            # Check a set of conditions to see if we
            # really want to linkify this document.
            bool1 = f[-3:]=='.md'       # only add markdown
            bool2 = f[-7:]!='_new.md'   # ignore _new.md (?)
            bool3 = '.github' not in fdir  # ignore github templates

            if( bool1 and bool2 and bool3):
                markdown_files.append( os.path.join( fdir, f ) )

    return markdown_files


def md_files_to_obj_dict(markdown_files):
    """
    Given a set of Markdown files, load each
    markdown file header and content. Then
    create the appropriate library object,
    and add it to obj_dict. When finished,
    return obj_dict.
    """
    obj_dict = {}

    errors = []
    n_total_files = 0
    n_error_files = 0
    for filename in markdown_files:
        n_total_files += 1

        # load markdown file + header
        header, content = parse_input_files.parse_library_md(filename)

        # create library object according to filename & header
        try:
            obj = create_library_object(filename, header, content)
        except KeyError as exc:
            errors.append(f'missing key in YAML header {filename}: {str(exc)}')
            n_error_files += 1
            continue

        if obj.ident in obj_dict:
            errors.append(f"{filename}: Duplicate identity: {obj.ident})")
            n_error_files += 1
            continue

        obj_dict[obj.ident] = obj

    if errors:
        error_string = "\n".join(errors)
        print(f"** ERROR: problems found in {n_error_files} of {n_total_files} files!")
        print(error_string)
        sys.exit(-1)

    return obj_dict

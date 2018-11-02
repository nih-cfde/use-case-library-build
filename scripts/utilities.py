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
    for obj in obj_dict.values():

        # User stories that aren't called from any epics
        if obj.obj_type=='USER STORY' and len(obj.epics)==0:
            warn = 'WARNING: orphaned user story {} has no parent epic!'.format(obj.ident)
            warnings.append(warn)

        # Epics that aren't called from any narratives
        if obj.obj_type=='EPIC' and obj.narrative is None:
            warn = 'WARNING: orphaned user epic {} has no parent narrative!'.format(obj.ident)
            warnings.append(warn)

        # Epics that don't have user stories
        if obj.obj_type=='EPIC' and len(obj.user_stories)==0:
            warn = 'WARNING: childless user epic {} has no user stories!'.format(obj.ident)
            warnings.append(warn)

        # Narratives that aren't called from any summaries
        if obj.obj_type=='NARRATIVE' and obj.summary is None:
            warn = 'WARNING: orphaned narrative {} has no parent summary!'.format(obj.ident)
            warnings.append(warn)

        # Narratives that don't have epics
        if obj.obj_type=='NARRATIVE' and len(obj.epics)==0:
            warn = 'WARNING: childless narrative {} has no epics!'.format(obj.ident)
            warnings.append(warn)

    warnings = sorted(warnings)
    for warning in warnings:
        print(warning)


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
    for filename in markdown_files:
        # load markdown file + header
        header, content = parse_input_files.parse_library_md(filename)

        # create library object according to filename & header
        obj = create_library_object(filename, header, content)
        if obj.ident in obj_dict:
            raise Exception("Duplicate identity: " + obj.ident)

        obj_dict[obj.ident] = obj

    return obj_dict


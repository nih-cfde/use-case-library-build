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
    for obj in obj_dict.values():

        # User stories that aren't called from any epics
        if obj.obj_type=='USER STORY' and len(self.epics)==0:
            print('WARNING: orphaned user story {} has no parent epic!'.format(obj.ident))

        # Epics that aren't called from any narratives
        if obj.obj_type=='EPIC' and self.narrative is None:
            print('WARNING: orphaned user epic {} has no parent narrative!'.format(obj.ident))

        # Epics that don't have user stories
        if obj.obj_type=='EPIC' and len(self.user_stories)==0:
            print('WARNING: orphaned user epic {} has no user stories!'.format(obj.ident))

        # Narratives that aren't called from any summaries
        if obj.obj_type=='NARRATIVE' and self.summary is None:
            print('WARNING: orphaned narrative {} has no parent summary!'.format(obj.ident))

        # Narratives that don't have epics
        if obj.obj_type=='NARRATIVE' and len(self.epics)==0:
            print('WARNING: orphaned narrative {} has no epics!'.format(obj.ident))


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
    Get the directory one path up from f
    """
    basepath = os.path.join(os.path.dirname(f), '..')
    basepath = os.path.abspath(basepath)
    return basepath

def subdir(basepath,location):
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


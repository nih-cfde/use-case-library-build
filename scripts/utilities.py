def scrub_overlap(tags):
    """
    For a given list of tags,
    look for tags that overlap with other tags,
    and if any are found, only keep the longer
    of the two tags.
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



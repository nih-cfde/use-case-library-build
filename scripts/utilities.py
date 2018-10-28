def scrub_overlap(tags):
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


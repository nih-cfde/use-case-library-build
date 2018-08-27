#! /usr/bin/env python
import sys
import argparse
import yaml


prefixes = {'EPIC': 'EPIC',
            'USERSTORY': 'USER STORY',
            'PER': 'PERSONA',
            'NARRATIVE': 'NARRATIVE'}


def get_type(filename):
    for prefix in prefixes:
        if filename.startswith(prefix):
            ident = filename.split('-', 2)
            return prefixes[prefix], "-".join(ident[:2])

    raise ValueError("unknown file type: " + filename)


def validate_header(filename, header):
    filetype, ident = get_type(filename)
    if filetype == 'PERSONA':
        print('persona', ident, header['name'], header['blurb'])
    elif filetype == 'USER STORY':
        print('user story', ident, header['title'], header['blurb'])
    elif filetype == 'NARRATIVE':
        print('narrative', ident, header['title'], header['persona'], header['blurb'])
        print('FOO', header['epics'])
    elif filetype == 'EPIC':
        print('epic', header['title'], header['blurb'])
        print('BAR', header['user-stories'])
    else:
        raise ValueError('unhandled file type: ' + filetype)


def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('inputfiles', nargs='+')
    args = p.parse_args(argv)

    for filename in args.inputfiles:
        lines = open(filename, 'rt').readlines()
        lines = [ x.rstrip() for x in lines ]
        assert lines[0].startswith('---')

        header_end = None
        for i, x in enumerate(lines[1:]):
            if x.startswith('---'):
                header_end = i+1
                break

        assert header_end, "no header found"

        # grab the yaml & the rest
        header = lines[0:i+1]
        rest = lines[i+2:]

        #print(header)
        #print(rest)
        yyheader = yaml.load("\n".join(header))

        validate_header(filename, yyheader)


if __name__ == '__main__':
    main()

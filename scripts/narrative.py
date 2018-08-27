#! /usr/bin/env python
import sys
import argparse

def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('inputfile')
    args = p.parse_args(argv)

    lines = open(args.inputfile, 'rt').readlines()
    lines = [ x.strip() for x in lines ]
    assert lines[0].startswith('---')

    header_end = None
    for i, x in enumerate(lines[1:]):
        if x.startswith('---'):
            header_end = i+1
            break

    assert header_end, "no header found"

    # grab the yaml & the rest
    header = lines[1:i]
    rest = lines[i+2:]

    print(header)
    print(rest)


if __name__ == '__main__':
    main()

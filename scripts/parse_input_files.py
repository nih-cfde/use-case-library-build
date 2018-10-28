"""
Parse the input files from library/, return yaml obj + content
"""
import yaml


def parse_library_md(filename):
    lines = open(filename, 'rt').readlines()
    lines = [ x.rstrip() for x in lines ]
    try:
        assert lines[0].startswith('---')
    except AssertionError:
        raise Exception("ERROR: Library file %s does not start with '---'"%(filename))

    header_end = None
    for i, x in enumerate(lines[1:]):
        if x.startswith('---'):
            header_end = i+1
            break

    try:
        assert header_end, "no header found"
    except AssertionError:
        raise Exception("ERROR: No header found in file %s"%(filename))


    # grab the yaml & the rest
    header = lines[0:i+1]
    rest = lines[i+2:]
    rest = "\n".join(rest)
    rest = rest.strip()

    try:
        yyheader = yaml.load("\n".join(header))
    except yaml.scanner.ScannerError:
        err = "Encountered scanner error while scanning YAML header\n"
        err += "File: %s\n"%(filename)
        err += "Header:\n"
        err += "\n".join(header)
        raise Exception(err)

    return yyheader, rest


def write_library_md(filename, header, content):
    with open(filename + '.fix', 'wt') as fp:
        fp.write('---\n')

        fp.write(yaml.dump(header))
        fp.write('---\n')
        fp.write(content)

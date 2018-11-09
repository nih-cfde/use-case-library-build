#!/usr/bin/env python
import os, re, sys
import glob


# Make first char of header values uppercase 
CASE='upper'


HALP = """
sed_fixes.py:
This script uses regular expressions to
perform fixes. It uses Python not sed, but 
the fixes are in the spirit of sed.

WARNING: This task will modify documents in the 
use case library.

Usage:

    ./sed_fixes.py <path-to-library>

Examples:

    Run from root dir of repo, specifying library dir:
    
        scripts/sed_fixes.sh library

    Run from this (scripts/) directory:

        ./sed_fixes.sh ../library
"""

def usage():
    print(HALP)
    sys.exit(1)

def main():

    libdir=""

    # Get some args
    if len(sys.argv)<2:
        usage()
    args = sys.argv[1:]

    # Set the location of the library and check it exists
    libdir = args[0]
    if not os.path.isdir(libdir):
        print('-'*40)
        print("ERROR: specified library location %s does not exist!"%(libdir))
        print('-'*40)
        usage()

    if CASE not in ['upper','lower']:
        print('-'*40)
        print("ERROR: invalid value specified for CASE, must be 'upper' or 'lower'")
        print('-'*40)
        usage()

    if not os.path.isfile(os.path.join(libdir,'USERSTORY-1.md')):
        print('-'*40)
        print("ERROR: no library files found in library loation %s (checked for USERSTORY-1.md)"%(libdir))
        print('-'*40)
        usage()

    # Assemble the search/replace patterns

    replacement_map = {}

    # Fullstops
    for label in ['title','input','output','task','title','persona','blurb']:

        # delete any fullstops at the end of a line
        k = r'(%s): (.*)\.\n'%(label)
        v = lambda p : '%s: %s'%(p.group(1),p.group(2))
        replacement_map[k] = v

    ## Capitalization
    for label in ['input','output','task','title','persona','blurb']:

        if CASE is 'upper':
            k = r'^(%s): ([a-z])'%(label)
            v = lambda p : '%s: %s'%(p.group(1),p.group(2).upper())
            replacement_map[k] = v

        else:
            k = r'^(%s): ([A-Z])'%(label)
            v = lambda p : '%s: %s'%(p.group(1),p.group(2).lower())
            replacement_map[k] = v

    # Acronyms
    replacement_map = {
        **replacement_map,
        r'[dD][bB][gG][aA][pP]'    : r'dbGaP',
        r'[tT][oO][pP][mM]ed'      : r'TOPMed',
        r'[cC][oO][pP][dD][gG]ene' : r'COPDGene',
        r'[gG][tT][eE]x'           : r'GTEx',
        r'jupyter'                 : r'Jupyter',
        r'python'                  : r'Python',
        r'rna-seq'                 : r'RNA-Seq',
        r'nIH'                     : r'NIH',
    }


    # Loop over each type and apply the regular expression

    types = ['EPIC','NARRATIVE','PERSONA','SUMMARY','USER']

    for t in types:

        print("sed_fixes.py running from %s, processing files of type %s"%(libdir,t))

        for g in glob.glob(os.path.join(libdir,'%s*'%(t))):

            # read
            with open(g,'r') as f:
                c = f.read()

            # replace
            for k in replacement_map:
                v = replacement_map[k]
                c = re.sub(k,v,c)

            # write
            with open(g,'w') as f:
                f.write(c)


    print("* "*20)
    print("sed_fixes.py finished scrubbing %s"%(libdir))


if __name__=="__main__":
    main()


#!/bin/bash

function usage() {
    echo ""
    echo ""
    echo "Use Case Library: sed fixes script"
    echo ""
    echo "This script takes an optional argument"
    echo "that is the relative path to the use case"
    echo "library directory. By default it is library/"
    echo ""
    echo "Examples:"
    echo ""
    echo "    Run from root dir of repo:"
    echo ""    
    echo "        scripts/sed_fixes.sh"
    echo ""
    echo "    Run from root dir of repo, specifying library dir:"
    echo ""    
    echo "        scripts/sed_fixes.sh library"
    echo ""
    echo "    Run from this (scripts/) directory:"
    echo ""
    echo "        ./sed_fixes.sh ../library"
    echo ""
    echo ""
    exit 1;
}

# ------------------
# Set library directory
LIBDIR=""

# Relative path to use case library
# (if not specified, assume user running it
#  from the root of the use-case-library repo)
if (( $# == 0 )); then
    LIBDIR="library"

elif (( $# == 1 )); then
    LIBDIR="$1"

else
    usage

fi

echo "Looking in directory \"$LIBDIR\" for use case library..."


# ---------------------
# Should first char of each line
# be changed to uppercase or lowercase?
# upper or lower
CASE="upper"


# -----------------------
# Should there be a fullstop at the
# end of each line?
# true or false
FULLSTOP="false"


# -----------------------
# Param checking

if [ "$CASE" != "upper" ] && [ "$CASE" != "lower" ]; then
    echo "ERROR: invalid value for CASE environment variable, must be 'upper' or 'lower'"
    usage
fi

if [ "$FULLSTOP" != "true" ] && [ "$FULLSTOP" != "false" ]; then
    echo "ERROR: invalid value for FULLSTOP environment variable, must be 'true' or 'false'"
    usage
fi


# -------------------------
# Now do the dang thing.

if [[ -f "$LIBDIR/USERSTORY-1.md" ]]; then

    # This is indeed the library directory

    for TYPE in EPIC NARRATIVE PERSONA SUMMARY USER; do

        echo "Running sed from $PWD, processing files in $LIBDIR of type $TYPE"

        # -----------------------------
        # Fix capitalization

        if [ "$CASE" == "upper" ]; then
            
            echo "Fixing capitalization (first character uppercase)..."

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \([a-z]\)/input: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \([a-z]\)/output: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \([a-z]\)/task: \u\1/g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \([a-z]\)/title: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \([a-z]\)/persona: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \([a-z]\)/blurb: \u\1/g' %

        elif [ "$CASE" == "lower" ]; then

            echo "Fixing capitalization (first character lowercase)..."

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \([A-Z]\)/input: \l\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \([A-Z]\)/output: \l\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \([A-Z]\)/task: \l\1/g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \([A-Z]\)/title: \l\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \([A-Z]\)/persona: \l\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \([A-Z]\)/blurb: \l\1/g' %

        fi

        # Fix these either way
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[dD][bB][gG][aA][pP]/dbGaP/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[tT][oO][pP][mM]ed/TOPMed/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[cC][oO][pP][dD][gG]ene/COPDGene/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[gG][tT][eE]x/GTEx/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/jupyter/Jupyter/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/python/Pupyter/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/rna-seq/RNA-Seq/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/nIH/NIH/g' %

        # -----------------------------
        # Fix punctuation

        echo "Fixing punctuation..."

        if [ "$FULLSTOP" == "true" ]; then

            # if no fullstop, add a fullstop

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \{1,\}\(.*\)[^\.]$/input: \1./g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \{1,\}\(.*\)[^\.]$/output: \1./g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\(.*\)[^\.]$/task: \1./g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \{1,\}\(.*\)[^\.]$/title: \1./g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \{1,\}\(.*\)[^\.]$/persona: \1./g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \{1,\}\(.*\)[^\.]$/blurb: \1./g' %

        elif [ "$FULLSTOP" == "false" ]; then

            # if fullstop, remove fullstop

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \{1,\}\(.*\)\.$/input: \1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \{1,\}\(.*\)\.$/output: \1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\(.*\)\.$/task: \1/g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \{1,\}\(.*\)\.$/title: \1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \{1,\}\(.*\)\.$/persona: \1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \{1,\}\(.*\)\.$/blurb: \1/g' %

        fi

    done

    echo "Done."

else

    if [[ -d "$LIBDIR" ]]; then
        echo "ERROR: The library directory \"$LIBDIR\" does not contain a USERSTORY-1.md file!"
    else
        echo "ERROR: The library directory \"$LIBDIR\" is not a directory!"
    fi

fi


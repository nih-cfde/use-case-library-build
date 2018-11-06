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
# be changed to uppercase?
# true or false
UPPERCASE="false"


# -----------------------
# Should there be a fullstop at the
# end of each line?
# true or false
FULLSTOP="false"

# -----------------------
# Param checking

if [ "$UPPERCASE" -ne "true" -a "$UPPERCASE" -ne "false" ]; then
    echo "ERROR: invalid value for UPPERCASE environment variable, must be 'true' or 'false'"
    usage
fi

if [ "$FULLSTOP" -ne "true" -a "$FULLSTOP" -ne "false" ]; then
    echo "ERROR: invalid value for FULLSTOP environment variable, must be 'true' or 'false'"
fi


# -------------------------
# Now do the dang thing.

if [[ -f "$LIBDIR/USERSTORY-1.md" ]]; then

    # This is indeed the library directory

    for TYPE in EPIC NARRATIVE PERSONA SUMMARY USER; do

        echo "Running sed from $PWD, processing files in $LIBDIR of type $TYPE"

        # -----------------------------
        # Fix capitalization

        if [ "$UPPERCASE" == "true" ]; then
            
            echo "Fixing capitalization (first character uppercase)..."

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \{1,\}\([a-z]\)/input: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \{1,\}\([a-z]\)/output: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\([a-z]\)/task: \u\1/g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \{1,\}\([a-z]\)/title: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \{1,\}\([a-z]\)/persona: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \{1,\}\([a-z]\)/blurb: \u\1/g' %

        elif [ "$UPPERCASE" == "false" ]; then

            echo "Fixing capitalization (first character lowercase)..."

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \{1,\}\([a-z]\)/input: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \{1,\}\([a-z]\)/output: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\([a-z]\)/task: \u\1/g' %

            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/title: \{1,\}\([a-z]\)/title: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/persona: \{1,\}\([a-z]\)/persona: \u\1/g' %
            ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/blurb: \{1,\}\([a-z]\)/blurb: \u\1/g' %

        fi

        # Fix these either way
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[dD][bB][gG][aA][pP]/dbGaP/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[tT][oO][pP][mM]ed/TOPMed/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/[cC][oO][pP][dD][gG]ene/COPDGene/g' %

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


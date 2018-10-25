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


# Now do the dang thing.
if [[ -f "$LIBDIR/USERSTORY-1.md" ]]; then

    # This is indeed the library directory

    for TYPE in EPIC NARRATIVE PERSONA SUMMARY USER; do

        echo "Running sed from $PWD, processing files in $LIBDIR of type $TYPE"

        echo "Fixing capitalization..."

        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \([a-z]\)/input: \u\1/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \([a-z]\)/output: \u\1/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\([a-z]\)/task: \u\1/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/DbGaP/dbGaP/g' %

        echo "Fixing punctuation..."

        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/input: \{1,\}\(.*\)\.$/input: \u\1/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/output: \{1,\}\(.*\)\.$/output: \u\1/g' %
        ls -1 ${LIBDIR}/${TYPE}* | xargs -n1 -I% sed -i 's/task: \{1,\}\(.*\)\.$/task: \u\1/g' %

    done

    echo "Done."

else
    if [[ -d "$LIBDIR" ]]; then
        echo "ERROR: The library directory \"$LIBDIR\" does not contain a USERSTORY-1.md file!"
    else
        echo "ERROR: The library directory \"$LIBDIR\" is not a directory!"
    fi

fi



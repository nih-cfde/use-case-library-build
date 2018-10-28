#! /usr/bin/env python
import sys
import os
from os.path import exists, isdir, join, abspath, dirname
import subprocess

# base UCL path
basepath = abspath(join(dirname(__file__), '..'))

def usage():
    print("copy_images.py script:")
    print("    This script copies a directory of images to the final ")
    print("    mkdocs documentation folder in output/.")
    print("    To use this script, pass the relative path to the images directory\n")
    print("         ./copy_images.py images\n")

def main():

    if len(sys.argv)<1:
        usage()
        sys.exit(1)

    imagedir = sys.argv[1]

    if exists(imagedir) and isdir(imagedir):
        subprocess.call(['cp','-r',imagedir,'output/docs/%s'%(imagedir)], cwd=basepath)
    
    sys.exit(0)

if __name__=="__main__":
    main()


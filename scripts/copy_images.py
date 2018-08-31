#! /usr/bin/env python
import sys
import os
from os.path import exists, isdir, join, abspath, dirname
import subprocess

basepath = join(dirname(__file__), '..')
basepath = abspath(basepath)

def usage():
    print("copy_images.py script:")
    print("  copies a directory of images to the final ")
    print("  mkdocs documentation folder in output/.")
    print("  pass in the name of the images directory:")
    print("         ./copy_images.py images")
    print("")

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


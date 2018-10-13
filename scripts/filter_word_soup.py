#!/usr/bin/env python
from panflute import *
import sys, os, re, json

from linkify_extract_word_soup import WORD_SOUP_FILE

def main(doc=None):
    return run_filter(
            linkify, 
            prepare=prepare, 
            finalize=finalize, 
            doc=doc
    )

def prepare(doc):
    doc.wordlist = []

def linkify(elem, doc):
    if type(elem)==Str:
        word = elem.text
        word = re.sub(r'\.$','',word)
        word = word.lower()
        doc.wordlist.append(word)

def finalize(doc):
    with open('wat.file','a') as f:
        f.write("\n".join(doc.wordlist))


if __name__=="__main__":
    main()

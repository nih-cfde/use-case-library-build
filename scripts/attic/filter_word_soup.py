#!/usr/bin/env python
from panflute import *
import sys, os, re, json

from extract_word_soup import WORD_SOUP_FILE
from extract_word_soup import STOP_WORD_LIST

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
        word = re.sub(r',$','',word)
        word = re.sub(r';$','',word)
        word = word.lower()
        if word not in STOP_WORD_LIST:
            doc.wordlist.append(word)

def finalize(doc):
    with open(WORD_SOUP_FILE,'a') as f:
        f.write("\n".join(doc.wordlist))


if __name__=="__main__":
    main()

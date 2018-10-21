#!/usr/bin/env python
import os, re, sys

import nltk
from nltk.collocations import *

"""
NLTK: Parse Word Soup and Generate Tags


Use the output of the extract_word_soup.py script
to process the word soup generated from the use case library
and compile a list of frequently-occurring words.

Step 1 is to run linkify_extract_word_soup.py and generate
word_soup.txt

Step 2 is to compile a list of most frequently-occurring
words and dump out a list of tags.

(Step 2.5 is to hand-edit the list of tags.)

Step 3 is to iterate over each item in the use case
library and determine which of the tags in the corpus
should be applied to that document. The YAML header
should be modified and the tags should be added.
"""


def step1_extract():
    pass


def step2_nltk():

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    
    # change this to read in your data
    finder = BigramCollocationFinder.from_words(
    
    
            nltk.corpus.genesis.words('blob.txt')
    
    
    )
    
    # only bigrams that appear 3+ times
    finder.apply_freq_filter(3) 
    
    # return the 5 n-grams with the highest PMI
    finder.nbest(bigram_measures.pmi, 5)  


if __name__=="__main__":


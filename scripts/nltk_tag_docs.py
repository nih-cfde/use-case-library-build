#!/usr/bin/env python
import os, re, sys

import nltk
from nltk.collocations import *

"""
NLTK: Tag Documentz

Using NLTK to tag use case library items
is a two step process.

Step 1:

Assemble words appearing in the use case library.

Use word frequencies from the entire corpus to 
create a set of tags to select from.

Save the tags corpus to a file, for hand editing.

Step 2:

Iterate over each item in the use case library
and determine which of the tags in the corpus 
appear in that document. Apply those tags.

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


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
5  Named Entity Recognition
----------------------------------------------------------------------
""")

sent = nltk.corpus.treebank.tagged_sents()[22]
print(nltk.ne_chunk(sent, binary=True))
print("-" * 40)

print(nltk.ne_chunk(sent))
print("-" * 40)

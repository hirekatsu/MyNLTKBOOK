# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
7.  Extracting Information from Text
----------------------------------------------------------------------
1  Information Extraction
----------------------------------------------------------------------
""")

locs = [('Omnicom', 'IN', 'New York'),
        ('DDB', 'IN', 'New York'),
        ('Kaplan Thaler Group', 'IN', 'New York'),
        ('BBDO South', 'IN', 'Atlanta'),
        ('Georgia-Pacific', 'IN', 'Atlanta')]
query = [e1 for (e1, rel, e2) in locs if e2 == 'Atlanta']
print(query)
print("-" * 40)


print("""
----------------------------------------------------------------------
1.1  Information Extraction Architecture
----------------------------------------------------------------------
""")


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
print("-" * 40)

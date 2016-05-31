# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
8.  Analyzing Sentence Structure
----------------------------------------------------------------------
1  Some Grammatical Dilemmas
1.1  Linguistic Data and Unlimited Possibilities
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
1.2  Ubiquitous Ambiguity
----------------------------------------------------------------------
""")

groucho_grammar = nltk.CFG.fromstring('''
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | V PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
''')

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)

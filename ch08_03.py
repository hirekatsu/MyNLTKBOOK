# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3  Context Free Grammar
3.1  A Simple Grammar
----------------------------------------------------------------------
""")

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> 'saw' | 'ate' | 'walked'
NP -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P -> 'in' | 'on' | 'by' | 'with'
""")

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

for tree in rd_parser.parse("the dog saw a man in the park".split()):
    print(tree)


print("""
----------------------------------------------------------------------
3.2  Writing Your Own Grammars
----------------------------------------------------------------------
""")

grammar1 = nltk.data.load('file:mygrammar.cfg')
sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)


print("""
----------------------------------------------------------------------
3.3  Recursion in Syntactic Structure
----------------------------------------------------------------------
""")

grammar2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
P -> 'on'
""")

rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse('the angry bear chased the frightened little squirrel'.split()):
    print(tree)
for tree in rd_parser.parse('Chatterer said Buster thought the tree was tall'.split()):
    print(tree)



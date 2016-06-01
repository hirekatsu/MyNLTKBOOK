# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
5  Dependencies and Dependency Grammar
----------------------------------------------------------------------
""")

groucho_dep_grammar = nltk.DependencyGrammar.fromstring('''
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
''')
print(groucho_dep_grammar)
print("-" * 40)

pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
    print(tree)
print("-" * 40)


print("""
----------------------------------------------------------------------
5.1  Valency and the Lexicon
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
5.2  Scaling Up
----------------------------------------------------------------------
""")
print("----- no code -----")

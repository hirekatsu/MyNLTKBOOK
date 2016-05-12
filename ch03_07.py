# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.7  Regular Expressions for Tokenizing Text
----------------------------------------------------------------------
""")

print("Simple Approaches to Tokenization")
raw = """When I'M a Duchess, 'she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""
print(re.split(r' ', raw))
print(re.split(r'[ \t\n]+', raw))
print("-" * 40)

print(re.split(r'\W+', raw))
print("-" * 40)

print(re.findall(r'\w+|\S\w*', raw))
print("-" * 40)

print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))
print("-" * 40)

print("NLTK's Regular Expression Tokenizer")
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r"""(?x)  #set flag to allow verbose regexps
((?:[A-Z]\.)+  # abbreviations, e.g. U.S.A.
|\w+(?:-\w+)*  # words with optional internal hypens
|\$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
|\.\.\.  #ellipsis
|[][.,;"'?():-_`])  # these are separate tokens; includes ],[
"""
print(nltk.regexp_tokenize(text, pattern))
print("-" * 40)

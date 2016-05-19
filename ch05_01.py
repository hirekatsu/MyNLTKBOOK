# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
5.  Categorizing and Tagging Words
----------------------------------------------------------------------
1  Using a Tagger
----------------------------------------------------------------------
""")

text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))
print("-" * 40)

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))
print("-" * 40)

print(nltk.pos_tag(word_tokenize('How to ski')))
print(nltk.pos_tag(word_tokenize('How the ski')))
print("-" * 40)

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
text.similar('bought')
text.similar('over')
text.similar('the')
print("-" * 40)


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.4  Regular Expressions for Detecting Word Patterns
----------------------------------------------------------------------
""")

print("Using Basic Meta-Characters")
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print([w for w in wordlist if re.search('ed$', w)])
print([w for w in wordlist if re.search('^..j..t..$', w)])
print("-" * 40)

print("Ranges and Closures")
print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)])
print("-" * 40)

print([w for w in wordlist if re.search('^[a-fj-o]+$', w)])
print("-" * 40)

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
print([w for w in chat_words if re.search('^m+i+n+e+$', w)])
print([w for w in chat_words if re.search('^[ha]+$', w)])
print("-" * 40)

wsj = sorted(set(nltk.corpus.treebank.words()))
print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)])
print([w for w in wsj if re.search('^[A-Z]+\$$', w)])
print([w for w in wsj if re.search('^[0-9]{4}$', w)])
print([w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)])
print([w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)])
print([w for w in wsj if re.search('(ed|ing)$', w)])
print("-" * 40)

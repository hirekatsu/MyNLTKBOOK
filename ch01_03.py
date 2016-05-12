# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

from nltk.book import *

print("""
----------------------------------------------------------------------
3  Computing with Language Simple Statistics
----------------------------------------------------------------------
""")

print(">>> saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']")
saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
print(">>> tokens = set(saying)")
tokens = set(saying)
print(">>> tokens = sorted(tokens)")
tokens = sorted(tokens)
print(">>> tokens[-2:]")
print(tokens[-2:])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.1  Frequency Distributions
----------------------------------------------------------------------
""")

print(">>> fdist1 = FreqDist(text1)")
fdist1 = FreqDist(text1)
print(">>> print(fdist1)")
print(fdist1)
print(">>> fdist1.most_common(50)")
print(fdist1.most_common(50))
print(">>> fdist1['whale']")
print(fdist1['whale'])
print("-" * 40)

print(">>> fdist2 = FreqDist(text2)")
fdist2 = FreqDist(text2)
print(">>> fdist2.most_common(50)")
print(fdist2.most_common(50))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.2  Fine-grained Selection of Words
----------------------------------------------------------------------
""")

print(">>> V = set(text1)")
V = set(text1)
print(">>> long_words = [w for w in V if len(w) > 15]")
long_words = [w for w in V if len(w) > 15]
print(">>> sorted(long_words)")
print(sorted(long_words))
print("-" * 40)

print(">>> fdist5 = FreqDist(text5)")
fdist5 = FreqDist(text5)
print(">>> sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)")
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Collocations and Bigrams
----------------------------------------------------------------------
""")

from nltk import bigrams
print(">>> list(bigrams['more', 'is', 'said', 'than', 'done'])")
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
print("-" * 40)

print(">>> text4.collocations()")
text4.collocations()
print(">>> text8.collocations()")
text8.collocations()
print("-" * 40)


print("""
----------------------------------------------------------------------
3.4  Counting Other Things
----------------------------------------------------------------------
""")

print(">>> [len(w) for w in text1]")
print([len(w) for w in text1])
print(">>> fdist = FreqDist(len(w) for w in text1)")
fdist = FreqDist(len(w) for w in text1)
print(">>> print(fdist)")
print(fdist)
print(">>> fdist")
print(fdist)
print("-" * 40)

print(">>> fdist.most_common()")
print(fdist.most_common())
print(">>> fdist.max()")
print(fdist.max())
print(">>> fdist[3]")
print(fdist[3])
print(">>> fdist.freq(3)")
print(fdist.freq(3))
print("-" * 40)


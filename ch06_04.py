# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4  Decision Trees
4.1  Entropy and Information Gain
----------------------------------------------------------------------
""")

import math


def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p, 2) for p in probs)

print(entropy(['male', 'male', 'male', 'male']))
print(entropy(['male', 'female', 'male', 'male']))
print(entropy(['female', 'male', 'female', 'male']))
print(entropy(['female', 'female', 'male', 'female']))
print(entropy(['female', 'female', 'female', 'female']))



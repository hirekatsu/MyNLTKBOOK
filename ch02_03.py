# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

print("""
----------------------------------------------------------------------
3  More Python: Reusing Code
3.1  Creating Programs with a Text Editor
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
3.2  Functions
----------------------------------------------------------------------
""")


def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
print(lexical_diversity(kjv))
print("-" * 40)


def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

print(plural('fairy'))
print(plural('woman'))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Modules
----------------------------------------------------------------------
""")
print("----- skipped -----")


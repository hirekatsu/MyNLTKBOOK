# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.6  Program Development
----------------------------------------------------------------------
""")

print("Structure of a Python Module")
print(nltk.translate.metrics.__file__)
print("-" * 40)

print("Multi-Module Programs")
print("----- no code -----")

print("Sources of Error")


def find_words(text, wordlength, result=[]):
    for word in text:
        if len(word) == wordlength:
            result.append(word)
    return result

print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 3))
print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 2, ['ur']))
print(find_words(['omg', 'teh', 'lolcat', 'sitted', 'on', 'teh', 'mat'], 3))
print("-" * 40)

print("Debugging Techniques")
# import pdb
# import mymodule
# pdb.run('mymodule.myfunction()')
print("-" * 40)

print("Defensive Programming")
print("----- no code -----")

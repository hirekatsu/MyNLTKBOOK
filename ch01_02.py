# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

from nltk.book import *


def lexical_diversity(text):
    return len(set(text))/len(text)


print("""
----------------------------------------------------------------------
2  A Closer Look at Python: Texts as Lists of Words
2.1  Lists
----------------------------------------------------------------------
""")

print(">>> sent1")
print(sent1)
print(">>> len(sent1)")
print(len(sent1))
print(">>> lexical_diversity(sent1)")
print(lexical_diversity(sent1))
print("-" * 40)

print(">>> sent2")
print(sent2)
print(">>> sent3")
print(sent3)
print("-" * 40)

ex1 = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
print(">>> sorted(ex1)")
print(sorted(ex1))
print(">>> len(set(ex1))")
print(len(set(ex1)))
print(">>> ex1.count('the')")
print(ex1.count('the'))
print("-" * 40)

print(">>> sent4 + sent1")
print(sent4 + sent1)
print("-" * 40)

print(">>> sent1.append('Some')")
sent1.append("Some")
print(">>> sent1")
print(sent1)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.2  Indexing Lists
----------------------------------------------------------------------
""")

print(">>> text4[173]")
print(text4[173])
print("-" * 40)

print(">>> text4.index('awaken')")
print(text4.index('awaken'))
print("-" * 40)

print(">>> text5[16715:16735]")
print(text5[16715:16735])
print(">>> text6[1600:1625]")
print(text6[1600:1625])
print("-" * 40)

print(">>> sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']")
sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
print(">>> sent[0]")
print(sent[0])
print(">>> sent[9]")
print(sent[9])
print("-" * 40)

print(">>> sent[5:8]")
print(sent[5:8])
print(">>> sent[5]")
print(sent[5])
print(">>> sent[6]")
print(sent[6])
print(">>> sent[7]")
print(sent[7])
print("-" * 40)

print(">>> sent[:3]")
print(sent[:3])
print(">>> text2[141525:]")
print(text2[141525:])
print("-" * 40)

print(">>> sent[0] = 'First'")
sent[0] = 'First'
print(">>> sent[9] = 'Last'")
sent[9] = 'Last'
print(">>> len(sent)")
print(len(sent))
print(">>> sent[1:9] = ['Second', 'Third']")
sent[1:9] = ['Second', 'Third']
print(">>> sent")
print(sent)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.3  Variables
----------------------------------------------------------------------
""")

print(">>> sent1 = ['Call', 'me', 'Ishmael', '.']")
sent1 = ['Call', 'me', 'Ishmael', '.']
print("-" * 40)

print(">>> my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']")
my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']
print(">>> noun_phrase = my_sent[1:4]")
noun_phrase = my_sent[1:4]
print(">>> noun_phrase")
print(noun_phrase)
print(">>> wOrDs = sorted(noun_phrase)")
wOrDs = sorted(noun_phrase)
print(">>> wOrDs")
print(wOrDs)
print("-" * 40)

print(">>> vocab = set(text1)")
vocab = set(text1)
print(">>> vocab_size = len(vocab)")
vocab_size = len(vocab)
print(">>> vocab_size")
print(vocab_size)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.4  Strings
----------------------------------------------------------------------
""")

print(">>> name = 'Monty'")
name = 'Monty'
print(">>> name[0]")
print(name[0])
print(">>> name[:4]")
print(name[:4])
print("-" * 40)

print(">>> name*2")
print(name*2)
print(">>> name+'!'")
print(name+'!')
print("-" * 40)

print(">>> ' '.join(['Monty', 'Python'])")
print(' '.join(['Monty', 'Python']))
print(">>> 'Monty Python'.split()")
print('Monty Python'.split())
print("-" * 40)

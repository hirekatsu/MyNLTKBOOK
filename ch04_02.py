# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.2  Sequences
----------------------------------------------------------------------
""")

t = 'walk', 'fem', 3
print(t)
print(t[0])
print(t[1:])
print(len(t))
print("-" * 40)

raw = 'I turned off the spectroroute'
text = ['I', 'turned', 'off', 'the', 'spectroroute']
pair = (6, 'turned')
print((raw[2], text[3], pair[1]))
print((raw[-3:], text[-3:], pair[-3:]))
print((len(raw), len(text), len(pair)))
print("-" * 40)

print("Operating on Sequence Types")
raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
text = word_tokenize(raw)
fdist = nltk.FreqDist(text)
print(sorted(fdist))
for key in fdist:
    print(key + ':', fdist[key], end=' ')
print()
print("-" * 40)

words = ['I', 'turned', 'off', 'the', 'spectroroute']
words[2], words[3], words[4] = words[3], words[4], words[2]
print(words)
print("-" * 40)

# tmp = words[2]
# words[2] = words[3]
# words[3] = words[4]
# words[4] = tmp

words = ['I', 'turned', 'off', 'the', 'spectroroute']
tags = ['noun', 'verb', 'prep', 'det', 'noun']
print(zip(words, tags))
print(list(zip(words, tags)))
print(list(enumerate(words)))
print("-" * 40)

text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
training_data, test_data = text[:cut], text[cut:]
print(text == training_data + test_data)
print(len(training_data) / len(test_data))
print("-" * 40)

print("Combining Different Sequence Types")
words = 'I turned off the spectroroute'.split()
wordlens = [(len(word), word) for word in words]
wordlens.sort()
print(' '.join(w for (_, w) in wordlens))
print("-" * 40)

lexicon = [
    ('the', 'det', ['Di:', 'D@']),
    ('off', 'prep', ['Qf', 'O:f'])
]
lexicon.sort()
lexicon[1] = ('turned', 'VBD', ['t3:nd', 't3`nd'])
del lexicon[0]
print("-" * 40)

print("Generator Expressions")
text = '''"When I use a word," Humpty Dumpty said in rather a scornful tone,
"it means just what I choose it to mean - neither more nor less."'''
print([w.lower() for w in word_tokenize(text)])
print("-" * 40)

print(max([w.lower() for w in word_tokenize(text)]))
print(max(w.lower() for w in word_tokenize(text)))
print("-" * 40)


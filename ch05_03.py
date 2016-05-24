# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3  Mapping Words to Properties Using Python Dictionaries
3.1  Indexing Lists vs Dictionaries
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
3.2  Dictionaries in Python
----------------------------------------------------------------------
""")

pos = {}
print(pos)
pos['colorless'] = 'ADJ'
print(pos)
pos['ideas'] = 'N'
pos['sleep'] = 'V'
pos['furiously'] = 'ADV'
print(pos)
print("-" * 40)

print(pos['ideas'])
print(pos['colorless'])
# print(pos['green'])
print("-" * 40)

for word in sorted(pos):
    print(word + ':', pos[word])
print("-" * 40)

print(list(pos.keys()))
print(list(pos.values()))
print(list(pos.items()))
for key, val in sorted(pos.items()):
    print(key + ':', val)
print("-" * 40)

pos['sleep'] = 'V'
print(pos['sleep'])
pos['sleep'] = 'N'
print(pos['sleep'])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Defining Dictionaries
----------------------------------------------------------------------
""")

pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
pos = dict(colorless='ADJ', ideas='N', sleep='V', furiously='ADV')
# pos = {['ideas', 'blogs', 'adventures'], 'N'}
print("-" * 40)


print("""
----------------------------------------------------------------------
3.4  Default Dictionaries
----------------------------------------------------------------------
""")

from collections import defaultdict
frequency = defaultdict(int)
frequency['colorless'] = 4
print(frequency['ideas'])
pos = defaultdict(list)
pos['sleep'] = ['NOUN', 'VERB']
print(pos['ideas'])
print("-" * 40)

pos = defaultdict(lambda: 'NOUN')
pos['colorless'] = 'ADJ'
print(pos['blog'])
print(list(pos.items()))
print("-" * 40)

alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = [word for (word, _) in vocab.most_common(1000)]
mapping = defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v] = v

alice2 = [mapping[v] for v in alice]
print(alice2[:100])
print(len(set(alice2)))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.5  Incrementally Updating a Dictionary
----------------------------------------------------------------------
""")

from collections import defaultdict
counts = defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    counts[tag] += 1
print(counts['NOUN'])
print(sorted(counts))

from operator import itemgetter
print(sorted(counts.items(), key=itemgetter(1), reverse=True))
print([t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)])
print("-" * 40)

pair = ('NP', 8336)
print(pair[1])
print(itemgetter(1)(pair))
print("-" * 40)

last_letters = defaultdict(list)
words = nltk.corpus.words.words('en')
for word in words:
    key = word[-2:]
    last_letters[key].append(word)
print(last_letters['ly'])
print(last_letters['zy'])
print("-" * 40)

anagrams = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
print(anagrams['aeilnrt'])
print("-" * 40)

anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
print(anagrams['aeilnrt'])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.6  Complex Keys and Values
----------------------------------------------------------------------
""")

pos = defaultdict(lambda: defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
    pos[(t1, w2)][t2] += 1
print(pos[('DET', 'right')])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.7  Inverting a Dictionary
----------------------------------------------------------------------
""")

counts = defaultdict(int)
for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
    counts[word] += 1
print([key for (key, value) in counts.items() if value == 32])
print("-" * 40)

pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
pos2 = dict((value, key) for (key, value) in pos.items())
print(pos2['N'])
print("-" * 40)

pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
pos2 = defaultdict(list)
for key, value in pos.items():
    pos2[value].append(key)
print(pos2['ADV'])
print("-" * 40)

pos2 = nltk.Index((value, key) for (key, value) in pos.items())
print(pos2['ADV'])
print("-" * 40)


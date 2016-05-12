# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.3  Questions of Style
----------------------------------------------------------------------
""")

print("Procedural vs Declarative Style")
tokens = nltk.corpus.brown.words(categories='news')
count = 0
total = 0
for token in tokens:
    count += 1
    total += len(token)
print(total / count)
print("-" * 40)

total = sum(len(t) for t in tokens)
print(total / len(tokens))
print("-" * 40)

# word_list = []
# i = 0
# while i < len(tokens):
#     j = 0
#     while j < len(word_list) and word_list[j] < tokens[i]:
#         j += 1
#     if j == 0 or tokens[i] != word_list[j-1]:
#         word_list.insert(j, tokens[i])
#     i += 1
#
# word_list = sorted(set(tokens))

fd = nltk.FreqDist(nltk.corpus.brown.words())
cumulative = 0.0
most_common_words = [word for (word, count) in fd.most_common()]
for rank, word in enumerate(most_common_words):
    cumulative += fd.freq(word)
    print("%3d %6.2f%% %s" % (rank + 1, cumulative * 100, word))
    if cumulative > 0.25:
        break
print("-" * 40)

text = nltk.corpus.gutenberg.words('milton-paradise.txt')
longest = ''
for word in text:
    if len(word) > len(longest):
        longest = word
print(longest)
print("-" * 40)

maxlen = max(len(word) for word in text)
print([word for word in text if len(word) == maxlen])
print("-" * 40)

print("Some Legitimate Uses for Counters")
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
n = 3
print([sent[i:i+n] for i in range(len(sent)-n+1)])
print("-" * 40)

m, n = 3, 7
array = [[set() for i in range(n)] for j in range(m)]
array[2][5].add('Alice')
pprint.pprint(array)
print("-" * 40)

array = [[set()]*n]*m
array[2][5].add(7)
pprint.pprint(array)
print("-" * 40)


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.9  Formatting: From Lists to Strings
----------------------------------------------------------------------
""")

print("From Lists to Strings")
silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
print(' '.join(silly))
print(';'.join(silly))
print(''.join(silly))
print("-" * 40)

print("Strings and Formats")
word = 'cat'
sentence = """hello
world"""
print(word)
print(sentence)
print("-" * 40)

fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in sorted(fdist):
    print(word, '->', fdist[word], end='; ')
print()
print("-" * 40)

for word in sorted(fdist):
    print('{}->{};'.format(word, fdist[word]), end=' ')
print()
print("-" * 40)

print('{}->{};'.format('cat', 3))
print("-" * 40)

print('{}->'.format('cat'))
print('{}'.format(3))
print('I want a {} right now'.format('coffee'))
print("-" * 40)

print('{} wants a {} {}'.format('Lee', 'sandwich', 'for lunch'))
# print('{} wants a {} {}'.format('sandwich', 'for lunch'))
print("-" * 40)

print('{} wants a {}'.format('Lee', 'sandwich', 'for lunch'))
print("-" * 40)

print('from {1} to {0}'.format('A', 'B'))
print("-" * 40)

template = 'Lee wants a {} right now'
menu = ['sandwich', 'spam fritter', 'pancake']
for snack in menu:
    print(template.format(snack))
print("-" * 40)

print("Lining Things Up")
print('{:6}'.format(41))
print('{:<6}'.format(41))
print("-" * 40)

print('{:6}'.format('dog'))
print('{:>6}'.format('dog'))

import math
print('{:.4f}'.format(math.pi))
print("-" * 40)

count, total = 3205, 9375
print('accuracy for {} words: {:.4%}'.format(total, count/total))
print("-" * 40)


def tabulate(cfdist, words, categories):
    print('{:16}'.format('Category'), end=' ')
    for word in words:
        print('{:>6}'.format(word), end=' ')
    print()
    for category in categories:
        print('{:16}'.format(category), end=' ')
        for word in words:
            print('{:6}'.format(cfdist[category][word]), end=' ')
        print()

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
tabulate(cfd, modals, genres)
print("-" * 40)

# print('{:{width}}' % ('Monty Python', width=15))
print('{:{width}}'.format('Monty Python', width=15))
print("-" * 40)

print("Writing Results to a File")
output_file = open('output.txt', 'w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    print(word, file=output_file)

print(len(words))
print(str(len(words)))
print(str(len(words)), file=output_file)
print("-" * 40)

print("Text Wrapping")
saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
for word in saying:
    print(word, '(' + str(len(word)) + '),', end=' ')
print()
print("-" * 40)

from textwrap import fill
format = '%s (%d)'
pieces = [format % (word, len(word)) for word in saying]
output = ' '.join(pieces)
wrapped = fill(output)
print(wrapped)
print("-" * 40)




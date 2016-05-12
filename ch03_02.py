# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.2  Strings: Text Processing at the Lowest Level
----------------------------------------------------------------------
""")

monty = 'Monty Python'
print(monty)
circus = "Monty Python's Flying Circus"
print(circus)
circus = 'Monty Python\'s Flying Circus'
print(circus)
print("-" * 40)

couplet = "Shall I compare thee to a Summer's day?"\
    'Thou are more lovely and more temperate:'
print(couplet)
couplet = ("Rough winds do shake the darling buds of May,"
           "And Summer's lease hath all too short a date:")
print(couplet)
print("-" * 40)

couplet = """Shall I compare thee to a Summer's day?
Thou are more lovely and more temperate:"""
print(couplet)
couplet = '''Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:'''
print(couplet)
print("-" * 40)

print('very' + 'very' + 'very')
print('very' * 3)
print("-" * 40)

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
    print(line)
print("-" * 40)

print("Printing Strings")
print(monty)
print("-" * 40)

grail = 'Holy Grail'
print(monty + grail)
print(monty, grail)
print(monty, 'and the', grail)

print("Accessing Individual Characters")
print(monty[0])
print(monty[3])
print(monty[5])
print("-" * 40)

print(monty[-1])
print(monty[5])
print(monty[-7])
print("-" * 40)

sent = 'colorless green ideas sleep furiously'
for char in sent:
    print(char, end=' ')
print()
print("-" * 40)

from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
print(fdist.most_common(5))
print([char for (char, count) in fdist.most_common()])
print("-" * 40)

print("Accessing Substrings")
print(monty[6:10])
print(monty[-12:-7])
print(monty[:5])
print(monty[6:])
phrase = 'And now for something completely different'
if 'thing' in phrase:
    print('found "thing"')
print(monty.find('Python'))
print("-" * 40)

print("The Difference between Lists and Strings")
query = 'Who knows?'
beatles = ['John', 'Paul', 'George', 'Ringo']
print(query[2])
print(beatles[2])
print(query[:2])
print(beatles[:2])
print(query + " I don't")
# beatles + 'Brian'
print(beatles + ['Brian'])
print("-" * 40)

beatles[0] = 'John Lennon'
del beatles[-1]
print(beatles)
print("-" * 40)

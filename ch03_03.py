# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import codecs

print("""
----------------------------------------------------------------------
3.3  Text Processing with Unicode
----------------------------------------------------------------------
""")

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = codecs.open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line)
print("-" * 40)

f = codecs.open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
print("-" * 40)

print(ord(u'ń'))
nacute = '\u0144'
print(nacute)
print(nacute.encode('utf8'))
print("-" * 40)

import unicodedata
lines = codecs.open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))
for c in line:
    if ord(c) > 127:
        print('{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))
print("-" * 40)

print(line.find('zosta\u0142y'))
line = line.lower()
print(line)
print(line.encode('unicode_escape'))
m = re.search(u'\u015b\w*', line)
print(m.group())
print("-" * 40)

print(word_tokenize(line))
print("-" * 40)

print("Using your local encoding in Python")
print("----- skipped -----")

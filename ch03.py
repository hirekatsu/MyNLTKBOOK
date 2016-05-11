# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import codecs


print("""
----------------------------------------------------------------------
3  Processing Raw Text
3.1  Accessing Text from the Web and from Disk
(any key to continue)""")
raw_input()
print("-" * 40)

print("Electronic Books")
import urllib2
url = 'http://www.gutenberg.org/files/2554/2554.txt'
response = urllib2.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:75])
print("-" * 40)

tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])
print("-" * 40)

text = nltk.Text(tokens)
print(type(text))
print(text[1024:1062])
text.collocations()
print("-" * 40)

print(raw.find('PART I'))
print(raw.rfind("End of Project Gutenberg's Crime"))
raw = raw[5338:1157743]
print(raw.find('PART I'))
print("-" * 40)

print("Dealing with HTML")
url = 'http://www.reuters.com/article/us-southchinasea-usa-china-idUSKCN0Y10DM'
html = urllib2.urlopen(url).read().decode('utf8')
print(html[:60])
print("-" * 40)

from bs4 import BeautifulSoup
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
print(tokens)
print("-" * 40)

tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')
print("-" * 40)

print("Processing RSS Feeds")
import feedparser
llog = feedparser.parse('http://languagelog.ldc.upenn.edu/nll/?feed=atom')
print(llog['feed']['title'])
print(len(llog.entries))
post = llog.entries[2]
print(post.title)
content = post.content[0].value
print(content[:70])
raw = BeautifulSoup(content).get_text()
print(word_tokenize(raw))
print("-" * 40)

print("Reading Local Files")
path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw = open(path, 'rU').read()
print("-" * 40)


print("""
----------------------------------------------------------------------
3.2  Strings: Text Processing at the Lowest Level
(any key to continue)""")
raw_input()
print("-" * 40)

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


print("""
----------------------------------------------------------------------
3.3  Text Processing with Unicode
(any key to continue)""")
raw_input()
print("-" * 40)

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

print(ord('ń'))
nacute = '\u0144'
print(nacute)
print(nacute.encode('utf8'))
print("-" * 40)

import unicodedata
lines = codecs.open(path, encoding='latin2').readliens()
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
m = re.search('\u015b\w*', line)
print(m.group())
print("-" * 40)

print(word_tokenize(line))
print("-" * 40)

print("Using your local encoding in Python")
print("----- skipped -----")



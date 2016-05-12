# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3  Processing Raw Text
3.1  Accessing Text from the Web and from Disk
----------------------------------------------------------------------
""")

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

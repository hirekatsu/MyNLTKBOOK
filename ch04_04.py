# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.4  Functions: The Foundation of Structured Programming
----------------------------------------------------------------------
""")


def get_text(file):
    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub(r'<.*>', '', text)
    text = re.sub('\s+', '', text)
    return text

print("Function Inputs and Outputs")


def repeat(msg, num):
    return ' '.join([msg] * num)

monty = 'Monty Python'
print(repeat(monty, 3))
print("-" * 40)

def monty():
    return 'Monty Python'

print(monty())
print("-" * 40)

print(repeat(monty(), 3))
print(repeat('Monty Python', 3))
print("-" * 40)


def my_sort1(mylist):
    mylist.sort()


def my_sort2(mylist):
    return sorted(mylist)


def my_sort3(mylist):
    mylist.sort()
    return mylist

print("Parameter Passing")
def set_up(word, properties):
    word = 'lolcat'
    properties.append('noun')
    properties = 5

w = ''
p = []
set_up(w, p)
print(w)
print(p)
print("-" * 40)

w = ''
word = w
word = 'lolcat'
print(w)
print("-" * 40)

p = []
properties = p
properties.append('noun')
properties = 5
print(p)
print("-" * 40)

print("Variable Scope")
print("----- no code -----")

print("Checking Parameter Types")


def tag(word):
    if word in ['a', 'the', 'all']:
        return 'det'
    else:
        return 'noun'

print(tag('the'))
print(tag('knight'))
print(tag(["'Tis", 'but', 'a', 'scratch']))
print("-" * 40)


def tag(word):
    assert isinstance(word, basestring), "argument to tag() must be a string"
    if word in ['a', 'the', 'all']:
        return 'det'
    else:
        return 'noun'

print("Functional Decomposition")
import urllib2
from bs4 import BeautifulSoup


def freq_words(url, freqdist, n):
    html = urllib2.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html, 'html.parser').get_text()
    for word in word_tokenize(raw):
        freqdist[word.lower()] += 1
    result = []
    for word, count in freqdist.most_common(n):
        result = result + [word]
    print(result)

constitution = "http://www.archives.gov/exhibits/charters/constitution_transcript.html"
fd = nltk.FreqDist()
freq_words(constitution, fd, 30)
print("-" * 40)


def freq_words(url, n):
    html = urllib2.urlopen(url).read().decode('utf8')
    text = BeautifulSoup(html, 'html.parser').get_text()
    freqdist = nltk.FreqDist(word.lower() for word in word_tokenize(text))
    return [word for (word, _) in freqdist.most_common(n)]

print(freq_words(constitution, 30))
print("-" * 40)

print("Documenting Functions")
print("----- skipped -----")

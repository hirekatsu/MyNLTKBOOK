# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.7  Algorithm Design
----------------------------------------------------------------------
""")

print("Recursion")


def factorial1(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    return result


def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)


def size1(s):
    return 1 + sum(size1(child) for child in s.hyponyms())


def size2(s):
    layer = [s]
    total = 0
    while layer:
        total += len(layer)
        layer = [h for c in layer for h in c.hyponyms()]
    return total

from nltk.corpus import wordnet as wn
dog = wn.synset('dog.n.01')
print(size1(dog))
print(size2(dog))
print("-" * 40)


def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value

trie = {}
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
insert(trie, 'chair', 'flesh')
insert(trie, 'chic', 'stylish')
trie = dict(trie)
print(trie['c']['h']['a']['t']['value'])
pprint.pprint(trie, width=40)
print("-" * 40)

print("Space-Time Tradeoffs")


def raw(file):
    contents = open(file).read()
    contents = re.sub(r'<.*?>', ' ', contents)
    contents = re.sub('\s+', ' ', contents)
    return contents


def snippet(doc, term):
    text = ' '*30 + raw(doc) + ' '*30
    pos = text.index(term)
    return text[pos-30:pos+30]

print("Building Index...")
files = nltk.corpus.movie_reviews.abspaths()
idx = nltk.Index((w, f) for f in files for w in raw(f).split())
query = ''
while query != 'quit':
    query = raw_input('query> ').strip()  # use input() in Python 3
    if query in idx:
        for doc in idx[query]:
            print(snippet(doc, query))
    else:
        print('Not found')
print("-" * 40)


def preprocess(tagged_corpus):
    words = set()
    tags = set()
    for sent in tagged_corpus:
        for word, tag in sent:
            words.add(word)
            tags.add(tag)
    wm = dict((w, i) for (i, w) in enumerate(words))
    tm = dict((t, i) for (i, t) in enumerate(tags))
    return [[(wm[w], tm[t]) for (w, t) in sent] for sent in tagged_corpus]

from timeit import Timer
vocab_size = 100000
setup_list = "import random; vocab = range(%d)" % vocab_size
setup_set = "import random; vocab = set(range(%d))" % vocab_size
statement = "random.randint(0, %d) in vocab" % (vocab_size * 2)
print(Timer(statement, setup_list).timeit(1000))
print(Timer(statement, setup_set).timeit(1000))
print("-" * 40)

print("Dynamic Programming")


def virahanka1(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in virahanka1(n-1)]
        l = ['L' + prosody for prosody in virahanka1(n-2)]
        return s + l


def virahanka2(n):
    lookup = [[''], ['S']]
    for i in range(n-1):
        s = ['S' + prosody for prosody in lookup[i+1]]
        l = ['L' + prosody for prosody in lookup[i]]
        lookup.append(s + l)
    return lookup[n]


def virahanka3(n, lookup={0:[''], 1:['S']}):
    if n not in lookup:
        s = ['S' + prosody for prosody in virahanka3(n-1)]
        l = ['L' + prosody for prosody in virahanka3(n-2)]
        lookup[n] = s + l
    return lookup[n]


from nltk import memoize
@memoize
def virahanka4(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in virahanka4(n-1)]
        l = ['L' + prosody for prosody in virahanka4(n-2)]
        return s + l

print(virahanka1(4))
print(virahanka2(4))
print(virahanka3(4))
print(virahanka4(4))
print("-" * 40)


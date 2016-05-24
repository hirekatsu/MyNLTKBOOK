# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
5  N-Gram Tagging
5.1  Unigram Tagging
----------------------------------------------------------------------
""")

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.tag(brown_sents[2007]))
print(unigram_tagger.evaluate(brown_tagged_sents))
print("-" * 40)


print("""
----------------------------------------------------------------------
5.2  Separating the Training and Testing Data
----------------------------------------------------------------------
""")

size = int(len(brown_tagged_sents) * 0.9)
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents))
print("-" * 40)


print("""
----------------------------------------------------------------------
5.3  General N-Gram Tagging
----------------------------------------------------------------------
""")

bigram_tagger = nltk.BigramTagger(train_sents)
print(bigram_tagger.tag(brown_sents[2007]))
unseen_sent = brown_sents[4203]
print(bigram_tagger.tag(unseen_sent))
print("-" * 40)

print(bigram_tagger.evaluate(test_sents))
print("-" * 40)


print("""
----------------------------------------------------------------------
5.4  Combining Taggers
----------------------------------------------------------------------
""")

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.evaluate(test_sents))
print("-" * 40)

t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print(t3.evaluate((test_sents)))
print("-" * 40)


print("""
----------------------------------------------------------------------
5.5  Tagging Unknown Words
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
5.6  Storing Taggers
----------------------------------------------------------------------
""")

from pickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()
print("-" * 40)

from pickle import load
input = open('t2.pkl', 'rb')
tagger = load(input)
input.close()
print("-" * 40)

text = """The board's action shows what free enterprise
is up against in our complex maze of regulatory laws ."""
tokens = text.split()
print(tagger.tag(tokens))


print("""
----------------------------------------------------------------------
5.7  Performance Limitations
----------------------------------------------------------------------
""")

cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in brown_tagged_sents for x, y, z in nltk.trigrams(sent))
ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print(sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N())

test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
print(nltk.ConfusionMatrix(gold_tags, test_tags))

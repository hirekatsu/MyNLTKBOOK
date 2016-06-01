# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3  Evaluation
3.1  The Test Set
----------------------------------------------------------------------
""")

import random
from nltk.corpus import brown
tagged_sents = list(brown.tagged_sents(categories='news'))
random.shuffle(tagged_sents)
size = int(len(tagged_sents) * 0.1)
train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]

file_ids = brown.fileids(categories='news')
size = int(len(file_ids) * 0.1)
train_sents = brown.tagged_sents(file_ids[size:])
test_sents = brown.tagged_sents(file_ids[:size])

train_sents = brown.tagged_sents(categories='news')
test_sents = brown.tagged_sents(categories='fiction')
print("-" * 40)

print("""
----------------------------------------------------------------------
3.2  Accuracy
----------------------------------------------------------------------
""")
train_set = [({'word': w}, t) for sent in train_sents for (w, t) in sent]
test_set = [({'word': w}, t) for sent in test_sents for (w, t) in sent]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Accurary: {:4.2f}'.format(nltk.classify.accuracy(classifier, test_set)))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Precision and Recall
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
3.4  Confusion Metrices
----------------------------------------------------------------------
""")


def tag_list(tagged_sents):
    return [tag for sent in tagged_sents for (word, tag) in sent]


def apply_tagger(tagger, corpus):
    return [tagger.tag(nltk.tag.untag(sent)) for sent in corpus]

t2 = nltk.BigramTagger(train_sents, backoff=nltk.UnigramTagger(train_sents, backoff=nltk.DefaultTagger('NN')))
gold = tag_list(brown.tagged_sents(categories='editorial'))
test = tag_list(apply_tagger(t2, brown.tagged_sents(categories='editorial')))
cm = nltk.ConfusionMatrix(gold, test)
print(cm.pretty_format(sort_by_count=True, show_percents=True, truncate=9))


print("""
----------------------------------------------------------------------
3.5  Cross-Validation
----------------------------------------------------------------------
""")
print("----- no code -----")

# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.3  Training Classifier-Based Chunkers
----------------------------------------------------------------------
""")

print("""THIS MODULE MAY TAKE VERY LONG TIME.
If you have MegaM installed on your computer, change the code to use it.
To continue this module, type 'yes'.""")
your_input = raw_input('continue? ').strip()
if your_input != 'yes':
    import sys
    sys.exit(0)

from nltk.corpus import conll2000
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])


class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(train_set, algorithm='iis', trace=0)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)


class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_sents = [[((w, t), c) for (w, t, c) in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w, t, c) for ((w, t), c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)


def npchunk_features_1(sentence, i, history):
    word, pos = sentence[i]
    return {'pos': pos}

npchunk_features = npchunk_features_1
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))
print("-" * 40)


def npchunk_features_2(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = '<START>', '<START>'
    else:
        prevword, prevpos = sentence[i-1]
    return {'pos': pos, 'prevpos': prevpos}

npchunk_features = npchunk_features_2
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))
print("-" * 40)


def npchunk_features_3(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = '<START>', '<START>'
    else:
        prevword, prevpos = sentence[i-1]
    return {'pos': pos, 'word': word, 'prevpos': prevpos}

npchunk_features = npchunk_features_3
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))
print("-" * 40)


def npchunk_features_4(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = '<START>', '<START>'
    else:
        prevword, prevpos = sentence[i-1]
    if i == len(sentence)-1:
        nextword, nextpos = '<END>', '<END>'
    else:
        nextword, nextpos = sentence[i+1]
    return {'pos': pos, 'word': word,
            'prevpos': prevpos, 'nextpos': nextpos,
            'prevpos+pos': '%s+%s' % (prevpos, pos),
            'pos+nextpos': '%s+%s' % (pos, nextpos),
            'tags-since-dt': tags_since_dt(sentence, i)}


def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))

npchunk_features = npchunk_features_4
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))
print("-" * 40)

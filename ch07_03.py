# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3  Developing and Evaluating Chunkers
3.1  Reading IOB Format and the CoNLL 2000 Corpus
----------------------------------------------------------------------
""")

text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
of IN B-PP
vice NN B-NP
chairman NN I-NP
of IN B-PP
Carlyle NNP B-NP
Group NNP I-NP
, , O
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()
print("-" * 40)

from nltk.corpus import conll2000
print(conll2000.chunked_sents('train.txt')[99])
print("-" * 40)

print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.2  Simple Evaluation and Baselines
----------------------------------------------------------------------
""")

from nltk.corpus import conll2000
cp = nltk.RegexpParser('')
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print(cp.evaluate(test_sents))
print("-" * 40)

grammar = r'NP: {<[CDJNP].*>+}'
cp = nltk.RegexpParser(grammar)
print(cp.evaluate(test_sents))
print("-" * 40)


class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))
print("-" * 40)

postags = sorted(set(pos for sent in train_sents for (word, pos) in sent.leaves()))
print(unigram_chunker.tagger.tag(postags))
print("-" * 40)


class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

bigram_chunker = BigramChunker(train_sents)
print(bigram_chunker.evaluate(test_sents))
print("-" * 40)


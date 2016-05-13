# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
2  Chunking
2.1  Noun Phrase Chunking
----------------------------------------------------------------------
""")

sentence = [('the', 'DT'), ('little', 'JJ'), ('yello', 'JJ'), ('dog', 'NN'),
            ('barked', 'VBD'), ('at', 'IN'), ('the', 'DT'), ('cat', 'NN')]
grammar = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.2  Tag Patterns
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
2.3  Chunking with Regular Expressions
----------------------------------------------------------------------
""")
grammar = r"""
 NP: {<DT|PP\$>?<JJ>*<NN>}  # chunk determiner/possessive, adjectives and noun
     {<NNP>+}                # chunk sequences of proper nouns
"""
cp = nltk.RegexpParser(grammar)
sentence = [('Rapunzel', 'NNP'), ('let', 'VBD'), ('down', 'RP'),
            ('her', 'PP$'), ('long', 'JJ'), ('golden', 'JJ'), ('hair', 'NN')]
print(cp.parse(sentence))
print("-" * 40)

nouns = [('money', 'NN'), ('market', 'NN'), ('fund', 'NN')]
grammar = 'NP: {<NN><NN>}  # chunk tow consecutive nouns'
cp = nltk.RegexpParser(grammar)
print(cp.parse(nouns))
print("-" * 40)


print("""
----------------------------------------------------------------------
2.4  Exploring Text Corpora
----------------------------------------------------------------------
""")
cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CHUNK': print(subtree)
print("-" * 40)


def find_chunks(chunkstring):
    label, _ = chunkstring.split(':', 1)
    cp = nltk.RegexpParser(chunkstring)
    brown = nltk.corpus.brown
    for sent in brown.tagged_sents():
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == label: print(subtree)

find_chunks('NOUNS: {<N.*><N.*><N.*><N.*>+}')
print("-" * 40)


print("""
----------------------------------------------------------------------
2.5  Chinking
----------------------------------------------------------------------
""")
grammar = r"""
 NP:
  {<.*>+}      # chunk everything
  }<VBD|IN>+{  # chink sequences of VBD and IN
"""
sentence = [('the', 'DT'), ('little', 'JJ'), ('yello', 'JJ'), ('dog', 'NN'),
            ('barked', 'VBD'), ('at', 'IN'), ('the', 'DT'), ('cat', 'NN')]
cp = nltk.RegexpParser(grammar)
print(cp.parse(sentence))
print("-" * 40)


print("""
----------------------------------------------------------------------
2.6  Representing Chunks: Tags vs Trees
----------------------------------------------------------------------
""")
print("----- no code -----")

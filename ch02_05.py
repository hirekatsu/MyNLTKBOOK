# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

import nltk
print("""
----------------------------------------------------------------------
5  WordNet
5.1  Senses and Synonyms
----------------------------------------------------------------------
""")

from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
print("-" * 40)

print(wn.synset('car.n.01').lemma_names())
print("-" * 40)

print(wn.synset('car.n.01').definition())
print(wn.synset('car.n.01').examples())
print("-" * 40)

print(wn.synset('car.n.01').lemmas())
print(wn.lemma('car.n.01.automobile'))
print(wn.lemma('car.n.01.automobile').synset())
print(wn.lemma('car.n.01.automobile').name())
print("-" * 40)

print(wn.synset('car'))
for synset in wn.synsets('car'):
    print(synset.lemma_names())
print("-" * 40)

print(wn.lemmas('car'))
print("-" * 40)

print(wn.synsets('dish'))
print(wn.synset('dish.n.01').lemma_names())
print(wn.synset('dish.n.01').definition())
print(wn.synset('dish.n.01').examples())
print(wn.synset('dish.n.01').lemmas())
print(wn.synset('dish.n.01.dish'))
print(wn.synset('dish.n.01.dish').synset())
print(wn.synset('dish.n.01.dish').name())
print("-" * 40)


print("""
----------------------------------------------------------------------
5.2  The WordNet Hierarchy
----------------------------------------------------------------------
""")

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar[0])
print(sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()))
print("-" * 40)

print(motorcar.hyponyms())
paths = motorcar.hypernym_paths()
print(len(paths))
print([synset.name() for synset in paths[0]])
print([synset.name() for synset in paths[1]])
print("-" * 40)

print(motorcar.root_hypernyms())
print("-" * 40)

nltk.app.wordnet()
print("-" * 40)


print("""
----------------------------------------------------------------------
5.3  More Lexical Relations
----------------------------------------------------------------------
""")

print(wn.synset('tree.n.01').part_meronyms())
print(wn.synset('tree.n.01').substance_meronyms())
print(wn.synset('tree.n.01').member_holonyms())
print("-" * 40)

for synset in wn.synsets('mint', wn.NOUN):
    print(synset.name() + ':', synset.definition())
print(wn.synset('mint.n.04').part_holonyms())
print(wn.synset('mint.n.04').substance_holonyms())
print("-" * 40)

print(wn.synset('walk.v.01').entailments())
print(wn.synset('eat.v.01').entailments())
print(wn.synset('tease.v.03').entailments())
print("-" * 40)

print(wn.lemma('supply.n.02.supply').antonms())
print(wn.lemma('rush.v.01.rush').antonyms())
print(wn.lemma('horizontal.a.01.horizontal').antonyms())
print(wn.lemma('staccato.r.01.staccato').antonyms())
print("-" * 40)


print("""
----------------------------------------------------------------------
5.4  Semantic Similarity
----------------------------------------------------------------------
""")

right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print(right.lowest_common_hypernyms(minke))
print(right.lowest_common_hypernyms(orca))
print(right.lowest_common_hypernyms(tortoise))
print(right.lowest_common_hypernyms(novel))
print("-" * 40)

print(wn.synset('baleen_whale.n.01').min_depth())
print(wn.synset('whale.n.02').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())
print(wn.synset('entity.n.01').min_depth())
print("-" * 40)

print(right.path_similarity(minke))
print(right.path_similarity(orca))
print(right.path_similarity(tortoise))
print(right.path_similarity(novel))
print("-" * 40)

# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
6  Relation Extraction
----------------------------------------------------------------------
""")

IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):
        print(nltk.sem.rtuple(rel))
print("-" * 40)

from nltk.corpus import conll2002
vnv = """
(
is/VI    # 3rd sing present and
was/VI   # past form of the verb zijn ('be')
werd/VI  # and also present
wordt/V  #past of worden('become')
)
.*       # followed by anything
van/Prep # followed by van ('of')
"""
VAN = re.complile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        print(nltk.sem.clause(r, relsym='VAN'))
print("-" * 40)

for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        print(nltk.sem.rtuple(r, lcon=True, rcon=True))
print("-" * 40)


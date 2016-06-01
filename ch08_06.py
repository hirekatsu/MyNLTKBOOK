# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
6  Grammar Development
6.1  Treebanks and Grammars
----------------------------------------------------------------------
""")

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)
print("-" * 40)


def filter(tree):
    child_nodes = [child.label() for child in tree if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)

from nltk.corpus import treebank
print([subtree for tree in treebank.parsed_sents() for subtree in tree.subtrees(filter)])
print("-" * 40)

from collections import defaultdict
entries = nltk.corpus.ppattach.attachments('training')
table = defaultdict(lambda: defaultdict(set))
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)

for key in sorted(table):
    if len(table[key]) > 1:
        print(key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V']))
print("-" * 40)

# nltk.corpus.sinca_treebank.parsed_sents()[3450].draw()
# print("-" * 40)


print("""
----------------------------------------------------------------------
6.2  Pernicious Ambiguity
----------------------------------------------------------------------
""")

grammar = nltk.CFG.fromstring('''
S -> NP V NP
NP -> NP Sbar
Sbar -> NP V
NP -> 'fish'
V -> 'fish'
''')
tokens = ['fish'] * 5
cp = nltk.ChartParser(grammar)
for tree in cp.parse(tokens):
    print(tree)
print("-" * 40)


print("""
----------------------------------------------------------------------
6.3  Weighted Grammar
----------------------------------------------------------------------
""")


def give(t):
    return t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' and (t[2].label() == 'PP-DTV' or t[2].label() == 'NP') and ('give' in t[0].leaves() or 'gave' in t[0].leaves())


def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')


def print_node(t, width):
    output = '%s %s: %s / %s: %s' % (sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
    if len(output) > width:
        output = output[:width] + '...'
    print(output)

for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):
        print_node(t, 72)
print("-" * 40)

grammar = nltk.PCFG.fromstring('''
S -> NP VP          [1.0]
VP -> TV NP         [0.4]
VP -> IV            [0.3]
VP -> DatV NP NP    [0.3]
TV -> 'saw'         [1.0]
IV -> 'ate'         [1.0]
DatV -> 'gave'      [1.0]
NP -> 'telescopes'  [0.8]
NP -> 'Jack'        [0.2]
''')
print(grammar)
print("-" * 40)

viterbi_parser = nltk.ViterbiParser(grammar)
for tree in viterbi_parser.parse(['Jack', 'saw', 'telescopes']):
    print(tree)
print("-" * 40)


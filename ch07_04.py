# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4  Recursion in Linguistic Structure
4.1  Building Nested Structure with Cascaded Chunkers
----------------------------------------------------------------------
""")

grammar = r"""
  NP: {<DT|JJ|NN.*>+}           # chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}                # chunk propositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$}  #chunk verbs and their arguments
  CLAUSE: {<NP><VP>}            # chunk NP, VP
"""
cp = nltk.RegexpParser(grammar)
sentence = [('May', 'NN'), ('saw', 'VBD'), ('the', 'DT'), ('cat', 'NN'),
            ('sit', 'VB'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')]
print(cp.parse(sentence))
print("-" * 40)

sentence = [('John', 'NNP'), ('thinks', 'VBZ'), ('Mary', 'NNP'), ('saw', 'VBD'),
            ('the', 'DT'), ('cat', 'NN'), ('sit', 'VB'), ('on', 'IN'), ('the', 'DT'), ('mat', 'NN')]
print(cp.parse(sentence))
print("-" * 40)

cp = nltk.RegexpParser(grammar, loop=2)
print(cp.parse(sentence))
print("-" * 40)


print("""
----------------------------------------------------------------------
4.2  Trees
----------------------------------------------------------------------
""")

tree1 = nltk.Tree('NP', ['Alice'])
print(tree1)
tree2 = nltk.Tree('NP', ['the', 'rabbit'])
print(tree2)
print("-" * 40)

tree3 = nltk.Tree('VP', ['cased', tree2])
tree4 = nltk.Tree('S', [tree1, tree3])
print(tree4)
print("-" * 40)

print(tree4[1])
print(tree4[1].label())
print(tree4.leaves())
print(tree4[1][1][1])
print("-" * 40)

tree3.draw()
print("-" * 40)


print("""
----------------------------------------------------------------------
4.3  Tree Traversal
----------------------------------------------------------------------
""")


def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=' ')
    else:
        # Now we know that t.node is defined
        print('(', t.label(), end=' ')
        for child in t:
            traverse(child)
        print(')', end=' ')
t = nltk.Tree('S', [nltk.Tree('NP', ['Alice']), nltk.Tree('VP', ['chased', nltk.Tree('NP', ['the', 'rabbit'])])])
print("-" * 40)
traverse(t)
print()
print("-" * 40)

# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4  Parsing With Context Free Grammar
4.1  Recursive Descent Parsing
----------------------------------------------------------------------
""")

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> 'saw' | 'ate' | 'walked'
NP -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P -> 'in' | 'on' | 'by' | 'with'
""")
rd_parser = nltk.RecursiveDescentParser(grammar1)
sent = 'Mary saw a dog'.split()
for tree in rd_parser.parse(sent):
    print(tree)
print("-" * 40)


print("""
----------------------------------------------------------------------
4.2  Shift-Reduce Parsing
----------------------------------------------------------------------
""")

sr_parser = nltk.ShiftReduceParser(grammar1)
sent = 'Mary saw a dog'.split()
for tree in sr_parser.parse(sent):
    print(tree)
print("-" * 40)

sr_parser = nltk.ShiftReduceParser(grammar1, trace=2)
for tree in sr_parser.parse(sent):
    print(tree)
print("-" * 40)


print("""
----------------------------------------------------------------------
4.3  The Left-Corner Parser
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
4.4  Well-Formed Substring Tables
----------------------------------------------------------------------
""")

groucho_grammar = nltk.CFG.fromstring('''
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | V PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
''')
text = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
print(groucho_grammar.productions(rhs=text[1]))
print("-" * 40)


def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        wfst[i][i+1] = productions[0].lhs()
    return wfst


def complete_wfst(wfst, tokens, grammar, trace=False):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1, nt2) in index:
                    wfst[start][end] = index[(nt1, nt2)]
                    if trace:
                        print('[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]' % (start, nt1, mid, nt2, end, start, index[(nt1, nt2)], end))
    return wfst


def display(wfst, tokens):
    print('\nWFST' + ' '.join(('%-4d' % i) for i in range(1, len(wfst))))
    for i in range(len(wfst)-1):
        print('%d  ' % i, end=' ')
        for j in range(1, len(wfst)):
            print('%-4s' % (wfst[i][j] or '.'), end=' ')
        print()

tokens = 'I shot an elephant in my pajamas'.split()
wfst0 = init_wfst(tokens, groucho_grammar)
display(wfst0, tokens)
wfst1 = complete_wfst(wfst0, tokens, groucho_grammar)
display(wfst1, tokens)
print("-" * 40)

wsft1 = complete_wfst(wfst0, tokens, groucho_grammar, trace=True)
print("-" * 40)

nltk.app.chartparser()
print("-" * 40)




# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

import nltk
print("""
----------------------------------------------------------------------
4  Lexical Resources
4.1  Wordlist Corpora
----------------------------------------------------------------------
""")


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
print(unusual_words(nltk.corpus.nps_chat.words()))
print("-" * 40)


from nltk.corpus import stopwords
print(stopwords.words('english'))
print("-" * 40)


def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

print(content_fraction(nltk.corpus.reuters.words()))
print("-" * 40)

puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
print([w for w in wordlist if len(w) >=6
       and obligatory in w
       and nltk.FreqDist(w) <= puzzle_letters])
print("-" * 40)

names = nltk.corpus.names
print(names.fileids())
male_names = names.words('male.txt')
female_names = names.words('female.txt')
print([w for w in male_names if w in female_names])
print("-" * 40)

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()
print("-" * 40)


print("""
----------------------------------------------------------------------
4.2  A Pronouncing Dictionary
----------------------------------------------------------------------
""")

entries = nltk.corpus.cmudict.entries()
print(len(entries))
for entry in entries[42371:42379]:
    print(entry)
print("-" * 40)

for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end=' ')
print()
print("-" * 40)

syllable = [u'N', u'IHO', u'K', u'S']
print([word for word, pron in entries if pron[-4:] == syllable])
print("-" * 40)

print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])
print(sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n')))
print("-" * 40)


def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])
print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])
print("-" * 40)

p3 = [(pron[0]+'-'+pron[2], word)
      for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3]
cfd = nltk.ConditionalFreqDist(p3)
for template in sorted(cfd.conditions()):
    if len(cfd[template]) > 10:
        words = sorted(cfd[template])
        wordstring = ' '.join(words)
        print(template, wordstring[:70] + '...')
print("-" * 40)

prondict = nltk.corpus.cmudict.dict()
print(prondict['fire'])
# print(prondict['blog'])
prondict['blog'] = [['B', 'L', 'AA1', 'G']]
print(prondict['blog'])
print("-" * 40)

text = ['natural', 'language', 'processing']
print([ph for w in text for ph in prondict[w][0]])
print("-" * 40)


print("""
----------------------------------------------------------------------
4.3  Comparative Wordlists
----------------------------------------------------------------------
""")

from nltk.corpus import swadesh
print(swadesh.fileids())
print(swadesh.words('en'))
print("-" * 40)

fr2en = swadesh.entries(['fr', 'en'])
print(fr2en)
translate = dict(fr2en)
print(translate['chien'])
print(translate['jeter'])
print("-" * 40)

de2en = swadesh.entries(['de', 'en'])
es2en = swadesh.entries(['es', 'en'])
translate.update(dict(de2en))
translate.update(dict(es2en))
print(translate['Hund'])
print(translate['perro'])
print("-" * 40)

languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139, 140, 141, 142]:
    print(swadesh.entries(languages)[i])
print("-" * 40)


print("""
----------------------------------------------------------------------
4.4  Shoebox and Toolbox Lexicons
----------------------------------------------------------------------
""")

from nltk.corpus import toolbox
print(toolbox.entries('rotokas.dic'))
print("-" * 40)


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
2  Tagged Corpora
2.1  Representing Tagged Tokens
----------------------------------------------------------------------
""")

tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
print(tagged_token[0])
print(tagged_token[1])
print("-" * 40)

sent = """
The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
said/VBD ''/'' ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN of/IN both/ABX governments/NNS "/" ./.
"""
print([nltk.tag.str2tuple(t) for t in sent.split()])
print("-" * 40)


print("""
----------------------------------------------------------------------
2.2  Reading Tagged Corpora
----------------------------------------------------------------------
""")

print(nltk.corpus.brown.tagged_words())
print(nltk.corpus.brown.tagged_words(tagset='universal'))
print("-" * 40)

print(nltk.corpus.nps_chat.tagged_words())
print(nltk.corpus.conll2000.tagged_words())
print(nltk.corpus.treebank.tagged_words())
print("-" * 40)

print(nltk.corpus.brown.tagged_words(tagset='universal'))
print(nltk.corpus.treebank.tagged_words(tagset='universal'))
print("-" * 40)

print(nltk.corpus.sinica_treebank.tagged_words())
print(nltk.corpus.indian.tagged_words())
print(nltk.corpus.mac_morpho.tagged_words())
print(nltk.corpus.conll2002.tagged_words())
print(nltk.corpus.cess_cat.tagged_words())
print("-" * 40)


print("""
----------------------------------------------------------------------
2.3  A Universal Part-of-Speech Tagset
----------------------------------------------------------------------
""")

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.most_common())
print("-" * 40)

tag_fd.plot(5, cumulative=True)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.4  Nouns
----------------------------------------------------------------------
""")

word_tag_pairs = nltk.bigrams(brown_news_tagged)
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']
fdist = nltk.FreqDist(noun_preceders)
print([tag for (tag, _) in fdist.most_common()])
print("-" * 40)


print("""
----------------------------------------------------------------------
2.5  Verbs
----------------------------------------------------------------------
""")

wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
print([wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'])
print("-" * 40)

cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['yield'].most_common())
print(cfd1['cut'].most_common())
print("-" * 40)

wsj = nltk.corpus.treebank.tagged_words()
cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
print(list(cfd2['VBN']))
print("-" * 40)

cfd3 = nltk.ConditionalFreqDist(wsj)
print([w for w in cfd3.conditions() if 'VBD' in cfd3[w] and 'VBN' in cfd3[w]])
idx1 = wsj.index(('kicked', 'VBD'))
print(wsj[idx1-4:idx1+1])
idx2 = wsj.index(('kicked', 'VBN'))
print(wsj[idx2-4:idx2+1])
print("-" * 40)

vbn_words = list(cfd2['VBN'])[:10]
for word in vbn_words:
    idx = wsj.index((word, 'VBN'))
    print(wsj[idx-1:idx], '->', word)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.6  Adjectives and Adverbs
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
2.7  Unsimplified Tags
----------------------------------------------------------------------
""")


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print(tag, tagdict[tag])
print("-" * 40)


print("""
----------------------------------------------------------------------
2.8  Exploring Tagged Corpora
----------------------------------------------------------------------
""")

brown_learned_text = brown.words(categories='learned')
print(sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often')))
print("-" * 40)

brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()
print("-" * 40)

from nltk.corpus import brown


def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if t1.startswith('V') and t2 == 'TO' and t3.startswith('V'):
            print(w1, w2, w3)

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
print("-" * 40)

brown_news_tagged = brown.tagged_words(categories='news')
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
for word in sorted(data.conditions()):
    if len(data[word]) > 3:
        tags = [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))
print("-" * 40)

nltk.app.concordance()
print("-" * 40)

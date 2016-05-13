# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

print("""
----------------------------------------------------------------------
2.  Accessing Text Corpora and Lexical Resources
----------------------------------------------------------------------
1  Accessing Text Corpora
1.1  Gutenberg Corpus
----------------------------------------------------------------------
""")

import nltk
print(">>> nltk.corpus.gutenberg.fileids()")
print(nltk.corpus.gutenberg.fileids())
print("-" * 40)

print(">>> emma = nltk.corpus.gutenberg.words('austen-emma.txt')")
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(">>> len(emma)")
print(len(emma))
print("-" * 40)

print(">>> emma = nltk.Text(emma)")
emma = nltk.Text(emma)
print(">>> emma.concordance('surprise')")
emma.concordance('surprise')
print("-" * 40)

from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
print("-" * 40)

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth_sentences)
print(macbeth_sentences[1116])
longest_len = max(len(s) for s in macbeth_sentences)
print([s for s in macbeth_sentences if len(s) == longest_len])
print("-" * 40)



print("""
----------------------------------------------------------------------
1.2  Web and Chat Text
----------------------------------------------------------------------
""")

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')
print("-" * 40)

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])
print("-" * 40)


print("""
----------------------------------------------------------------------
1.3  Brown Corpus
----------------------------------------------------------------------
""")

from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news', 'editorial', 'reviews']))
print("-" * 40)

news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ')
print()
print("-" * 40)

scifi_text = brown.words(categories='science_fiction')
fdis = nltk.FreqDist(w.lower() for w in scifi_text)
whwords = ['what', 'when', 'where', 'who', 'why', 'which']
for wh in whwords:
    print(wh + ':', fdist[wh], end=' ')
print()
print("-" * 40)

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
print("-" * 40)


print("""
----------------------------------------------------------------------
1.4  Reuters Corpus
----------------------------------------------------------------------
""")

from nltk.corpus import reuters
print(reuters.fileids())
print(reuters.categories())
print("-" * 40)

print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865', 'training/9880']))
print(reuters.fileids('barley'))
print(reuters.fileids(['barley', 'com']))
print("-" * 40)

print(reuters.words('training/9865')[:14])
print(reuters.words(['training/9865', 'training/9880']))
print(reuters.words(categories='barley'))
print(reuters.words(categories=['barley', 'com']))
print("-" * 40)


print("""
----------------------------------------------------------------------
1.5  Inaugural Address Corpus
(any key to continue)""")
raw_input()
print("-" * 40)

from nltk.corpus import inaugural
print(inaugural.fileids())
print([fileid[:4] for fileid in inaugural.fileids()])
print("-" * 40)

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()
print("-" * 40)


print("""
----------------------------------------------------------------------
1.6  Annotated Text Corpora
----------------------------------------------------------------------
""")
print("----- no code -----")


print("""
----------------------------------------------------------------------
1.7  Corpora in Other Languages
----------------------------------------------------------------------
""")

print(nltk.corpus.cess_esp.words())
print(nltk.corpus.floresta.words())
print(nltk.corpus.indian.words('hindi.pos'))
print(nltk.corpus.udhr.fileids())
print(nltk.corpus.udhr.words('Javanese-Latin1')[11:])
print("-" * 40)

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
print("-" * 40)


print("""
----------------------------------------------------------------------
1.8  Text Corpus Structure
----------------------------------------------------------------------
""")

raw = gutenberg.raw('burgess-busterbrown.txt')
print(raw[1:20])
words = gutenberg.words('burgess-busterbrown.txt')
print(words[1:20])
sents = gutenberg.sents('burgess-busterbrown.txt')
print(sents[1:20])
print("-" * 40)


print("""
----------------------------------------------------------------------
1.9  Loading your own Corpus
----------------------------------------------------------------------
""")
print("----- skipped -----")


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division


print("""
----------------------------------------------------------------------
1  Accessing Text Corpora
1.1  Gutenberg Corpus
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- no code -----")


print("""
----------------------------------------------------------------------
1.7  Corpora in Other Languages
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- skipped -----")


print("""
----------------------------------------------------------------------
2  Conditional Frequency Distributions
2.1  Conditions and Events
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- skipped -----")


print("""
----------------------------------------------------------------------
2.2  Counting Words by Genre
(any key to continue)""")
raw_input()
print("-" * 40)

# from nltk.corpus import brown
# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre))

genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)]
print(len(genre_word))
print("-" * 40)

print(genre_word[:4])
print(genre_word[-4:])
print("-" * 40)

cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
print(cfd.conditions())
print("-" * 40)

print(cfd['news'])
print(cfd['romance'])
print(cfd['romance'].most_common(20))
print(cfd['romance']['could'])
print("-" * 40)


print("""
----------------------------------------------------------------------
2.3  Plotting and Tabulating Distributions
(any key to continue)""")
raw_input()
print("-" * 40)

# from nltk.corpus import inaugural
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target))

# from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))
cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)
print("-" * 40)

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre))
samples = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cfd.tabulate(samples=samples)
cfd.plot(samples=samples)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.4  Generating Random Text with Bigrams
(any key to continue)""")
raw_input()
print("-" * 40)

sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
print(list(nltk.bigrams(sent)))
print("-" * 40)


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
    print()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print(cfd['living'])
generate_model(cfd, 'living')
print("-" * 40)


print("""
----------------------------------------------------------------------
3  More Python: Reusing Code
3.1  Creating Programs with a Text Editor
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- no code -----")


print("""
----------------------------------------------------------------------
3.2  Functions
(any key to continue)""")
raw_input()
print("-" * 40)


def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
print(lexical_diversity(kjv))
print("-" * 40)


def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

print(plural('fairy'))
print(plural('woman'))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Modules
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- skipped -----")


print("""
----------------------------------------------------------------------
4  Lexical Resources
4.1  Wordlist Corpora
(any key to continue)""")
raw_input()
print("-" * 40)


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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

from nltk.corpus import toolbox
print(toolbox.entries('rotokas.dic'))
print("-" * 40)


print("""
----------------------------------------------------------------------
5  WordNet
5.1  Senses and Synonyms
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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


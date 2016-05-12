# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
3.5  Useful Applications of Regular Expressions
----------------------------------------------------------------------
""")

print("Extracting Word Pieces")
word = 'supercalifragilisticexpialidocious'
print(re.findall(r'[aeiou]', word))
print(len(re.findall(r'[aeiou]', word)))
print("-" * 40)

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
print(fd.most_common(12))
print("-" * 40)

print([int(n) for n in re.findall(r'[0-9]+', '2009-12-31')])
print("-" * 40)

print("Doing More with Word Pieces")
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'


def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')
print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))
print("-" * 40)

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()
print("-" * 40)

cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['su'])
print(cv_index['po'])
print("-" * 40)

print("Finding Word Stems")
# def stem(word):
#     for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]
#     return word
print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes'))
print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes'))
print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language'))
print("-" * 40)


def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange woman lying in ponds distributing swords
is no basis for a system of government. Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
print([stem(t) for t in tokens])
print("-" * 40)

print("Searching Tokenized Text")
from nltk.corpus import gutenberg, nps_chat
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r'<a>(<.*>)<man>')
chat = nltk.Text(nps_chat.words())
chat.findall(r'<.*> <.*> <bro>')
chat.findall(r'<l.*>{3,}')
print("-" * 40)

nltk.re_show('kaa', ' '.join(rotokas_words))
nltk.app.nemo()
print("-" * 40)

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
hobbies_learned.findall(r'<\w*> <and> <other> <\w*s>')
print("-" * 40)

hobbies_learned.findall(r'<as> <\w*> <as> <\w*>')
print("-" * 40)

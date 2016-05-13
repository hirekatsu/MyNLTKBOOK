# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4.5  Doing More with Functions
----------------------------------------------------------------------
""")

print("Functions as Arguments")
sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',
        'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']


def extract_property(prop):
    return [prop(word) for word in sent]

print(extract_property(len))


def last_letter(word):
    return word[-1]

print(extract_property(last_letter))
print("-" * 40)

print(extract_property(lambda w: w[-1]))
print("-" * 40)

print(sorted(sent))
print(sorted(sent, cmp))
print(sorted(sent, lambda x, y: cmp(len(y), len(x))))
print("-" * 40)

print("Accumulative Functions")


def search1(substring, words):
    result = []
    for word in words:
        if substring in word:
            result.append(word)
    return result


def search2(substring, words):
    for word in words:
        if substring in word:
            yield word

for item in search1('zz', nltk.corpus.brown.words()):
    print(item, end=' ')
print()
for item in search2('zz', nltk.corpus.brown.words()):
    print(item, end=' ')
print()
print("-" * 40)


def permulations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in permulations(seq[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + seq[0:1] + perm[i:]

print(list(permulations(['police', 'fish', 'buffalo'])))
print("-" * 40)

print("Higher-Order Functions")


def is_content_word(word):
    return word.lower() not in ['a', 'of', 'the', 'and', 'will', ',', '.']

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
print(list(filter(is_content_word, sent)))
print([w for w in sent if is_content_word(w)])
print("-" * 40)

lengths = list(map(len, nltk.corpus.brown.sents(categories='news')))
print(sum(lengths) / len(lengths))
lengths = [len(sent) for sent in nltk.corpus.brown.sents(categories='news')]
print(sum(lengths) / len(lengths))
print("-" * 40)

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
print(list(map(lambda w: len(filter(lambda c: c.lower() in 'aeiou', w)), sent)))
print([len([c for c in w if c.lower() in 'aeiou']) for w in sent])
print("-" * 40)

print("Named Arguments")


def repeat(msg='<empty>', num=1):
    return msg * num

print(repeat(num=3))
print(repeat(msg='Alice'))
print(repeat(num=5, msg='Alice'))
print("-" * 40)


def generic(*args, **kwargs):
    print(args)
    print(kwargs)

generic(1, 'African swallow', monty='python')
print("-" * 40)

song = [['four', 'calling', 'birds'],
        ['three', 'French', 'hens'],
        ['two', 'turtle', 'doves']]
print(list(zip(song[0], song[1], song[2])))
print(list(zip(*song)))
print("-" * 40)


def freq_words(file, min=1, num=10):
    text = open(file).read()
    tokens = word_tokenize(text)
    freqdist = nltk.FreqDist(t for t in tokens if len(t) >= min)
    return freqdist.most_common(num)
# fw = freq_words('ch01.rst', 4, 10)
# fw = freq_words('ch01.rst', min=4, num=10)
# fw = freq_words('ch01.rst', num=10, min=4)
print("-" * 40)


def freq_words(file, min=1, num=10, verbose=False):
    freqdist = nltk.FreqDist()
    if verbose: print("Opening", file)
    text = open(file).read()
    if verbose: print("Read in %d characters" % len(text))
    for word in word_tokenize(text):
        if len(word) >= min:
            freqdist[word] += 1
            if verbose and freqdist.N() % 100 == 0: print(".", sep="")
    if verbose: print
    return freqdist.most_common(num)
print("-" * 40)

# with open('lexicon.txt') as f:
#     data = f.read()
#     # process the data

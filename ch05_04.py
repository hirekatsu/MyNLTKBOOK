# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4  Automatic Tagging
4.1  The Default Tagger
----------------------------------------------------------------------
""")

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags).max())
print("-" * 40)

raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print(default_tagger.tag(tokens))
print("-" * 40)

print(default_tagger.evaluate(brown_tagged_sents))
print("-" * 40)


print("""
----------------------------------------------------------------------
4.2  The Regular Expression Tagger
----------------------------------------------------------------------
""")

patterns = [
    (r'.*ing$', 'VBS'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')                     # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(brown_sents[3]))
print(regexp_tagger.evaluate(brown_tagged_sents))
print("-" * 40)


print("""
----------------------------------------------------------------------
4.3  The Lookup Tagger
----------------------------------------------------------------------
""")

fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.most_common(100)
likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print(baseline_tagger.evaluate(brown_tagged_sents))
print("-" * 40)

sent = brown.sents(categories='news')[3]
print(baseline_tagger.tag(sent))
print("-" * 40)

baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
print("-" * 40)


def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))


def display():
    import pylab
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()
print("-" * 40)


print("""
----------------------------------------------------------------------
4.4  Evaluation
----------------------------------------------------------------------
""")
print("----- no code -----")


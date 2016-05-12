# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

import nltk
from nltk.corpus import brown
from nltk.corpus import udhr
print("""
----------------------------------------------------------------------
2  Conditional Frequency Distributions
2.1  Conditions and Events
----------------------------------------------------------------------
""")
print("----- skipped -----")


print("""
----------------------------------------------------------------------
2.2  Counting Words by Genre
----------------------------------------------------------------------
""")

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
----------------------------------------------------------------------
""")

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
----------------------------------------------------------------------
""")

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

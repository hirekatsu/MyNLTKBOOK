# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division


print("""
----------------------------------------------------------------------
1  Computing with Language: Texts and Words
1.2  Getting Started with NLTK
----------------------------------------------------------------------
""")

print(">>> nltk.book import *")
from nltk.book import *
print("""
>>> text1
%s
>>> text2
%s
"""[1:-1] % (text1, text2))
print("-" * 40)

print("""
----------------------------------------------------------------------
1.3  Searching Text
----------------------------------------------------------------------
""")

print(">>> text1.concordance('monstrous')")
text1.concordance("monstrous")
print("-" * 40)

print(">>> text2.concordance('affection')")
text2.concordance("affection")
print(">>> text3.concordance('lived')")
text3.concordance("lived")
print("-" * 40)

print(">>> text1.similar('monstrous')")
text1.similar("monstrous")
print(">>> text2.similar('monstrous')")
text2.similar("monstrous")
print("-" * 40)

print(">>> text2.common_contexts(['monstrous', 'very'])")
text2.common_contexts(["monstrous", "very"])
print("-" * 40)

print(">>> text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])")
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
print("-" * 40)

# Text.generate() is not available in NLTK 3.0
# print(">>> text3.generate()"
# text3.generate()


print("""
----------------------------------------------------------------------
1.4  Counting Vocabulary
----------------------------------------------------------------------
""")

print(">>> len(text3)")
print(len(text3))
print("-" * 40)

print(">>> sorted(set(text3))")
print(sorted(set(text3)))
print(">>> len(set(text3))")
print(len(set(text3)))
print("-" * 40)

print(">>> len(set(text3))/len(text3)")
print(len(set(text3))/len(text3))
print("-" * 40)

print(">>> text3.count('smote')")
print(text3.count("smote"))
print(">>> 100*text4.count('a')/len(text4)")
print(100*text4.count('a')/len(text4))
print("-" * 40)

print(">>> text5.count('lol')")
print(text5.count('lol'))
print(">>> 100*text5.count('lol')/len(text5)")
print(100*text5.count('lol')/len(text5))
print("-" * 40)


def lexical_diversity(text):
    return len(set(text))/len(text)


def percentage(count, total):
    return 100 * count / total


print(">>> lexical_diversity(text3)")
print(lexical_diversity(text3))
print(">>> lexical_diversity(text5)")
print(lexical_diversity(text5))
print(">>> percentage(4, 5)")
print(percentage(4, 5))
print(">>> percentage(text4.count('a'), len(text4))")
print(percentage(text4.count('a'), len(text4)))
print("-" * 40)


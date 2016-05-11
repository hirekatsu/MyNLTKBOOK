# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

print("""
----------------------------------------------------------------------
1  Computing with Language: Texts and Words
1.2  Getting Started with NLTK
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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
(any key to continue)""")
raw_input()
print("-" * 40)

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


print("""
----------------------------------------------------------------------
2  A Closer Look at Python: Texts as Lists of Words
2.1  Lists
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> sent1")
print(sent1)
print(">>> len(sent1)")
print(len(sent1))
print(">>> lexical_diversity(sent1)")
print(lexical_diversity(sent1))
print("-" * 40)

print(">>> sent2")
print(sent2)
print(">>> sent3")
print(sent3)
print("-" * 40)

ex1 = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
print(">>> sorted(ex1)")
print(sorted(ex1))
print(">>> len(set(ex1))")
print(len(set(ex1)))
print(">>> ex1.count('the')")
print(ex1.count('the'))
print("-" * 40)

print(">>> sent4 + sent1")
print(sent4 + sent1)
print("-" * 40)

print(">>> sent1.append('Some')")
sent1.append("Some")
print(">>> sent1")
print(sent1)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.2  Indexing Lists
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> text4[173]")
print(text4[173])
print("-" * 40)

print(">>> text4.index('awaken')")
print(text4.index('awaken'))
print("-" * 40)

print(">>> text5[16715:16735]")
print(text5[16715:16735])
print(">>> text6[1600:1625]")
print(text6[1600:1625])
print("-" * 40)

print(">>> sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']")
sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
print(">>> sent[0]")
print(sent[0])
print(">>> sent[9]")
print(sent[9])
print("-" * 40)

print(">>> sent[5:8]")
print(sent[5:8])
print(">>> sent[5]")
print(sent[5])
print(">>> sent[6]")
print(sent[6])
print(">>> sent[7]")
print(sent[7])
print("-" * 40)

print(">>> sent[:3]")
print(sent[:3])
print(">>> text2[141525:]")
print(text2[141525:])
print("-" * 40)

print(">>> sent[0] = 'First'")
sent[0] = 'First'
print(">>> sent[9] = 'Last'")
sent[9] = 'Last'
print(">>> len(sent)")
print(len(sent))
print(">>> sent[1:9] = ['Second', 'Third']")
sent[1:9] = ['Second', 'Third']
print(">>> sent")
print(sent)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.3  Variables
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> sent1 = ['Call', 'me', 'Ishmael', '.']")
sent1 = ['Call', 'me', 'Ishmael', '.']
print("-" * 40)

print(">>> my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']")
my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']
print(">>> noun_phrase = my_sent[1:4]")
noun_phrase = my_sent[1:4]
print(">>> noun_phrase")
print(noun_phrase)
print(">>> wOrDs = sorted(noun_phrase)")
wOrDs = sorted(noun_phrase)
print(">>> wOrDs")
print(wOrDs)
print("-" * 40)

print(">>> vocab = set(text1)")
vocab = set(text1)
print(">>> vocab_size = len(vocab)")
vocab_size = len(vocab)
print(">>> vocab_size")
print(vocab_size)
print("-" * 40)


print("""
----------------------------------------------------------------------
2.4  Strings
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> name = 'Monty'")
name = 'Monty'
print(">>> name[0]")
print(name[0])
print(">>> name[:4]")
print(name[:4])
print("-" * 40)

print(">>> name*2")
print(name*2)
print(">>> name+'!'")
print(name+'!')
print("-" * 40)

print(">>> ' '.join(['Monty', 'Python'])")
print(' '.join(['Monty', 'Python']))
print(">>> 'Monty Python'.split()")
print('Monty Python'.split())
print("-" * 40)


print("""
----------------------------------------------------------------------
3  Computing with Language Simple Statistics
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']")
saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
print(">>> tokens = set(saying)")
tokens = set(saying)
print(">>> tokens = sorted(tokens)")
tokens = sorted(tokens)
print(">>> tokens[-2:]")
print(tokens[-2:])
print("-" * 40)


print("""
----------------------------------------------------------------------
3.1  Frequency Distributions
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> fdist1 = FreqDist(text1)")
fdist1 = FreqDist(text1)
print(">>> print(fdist1)")
print(fdist1)
print(">>> fdist1.most_common(50)")
print(fdist1.most_common(50))
print(">>> fdist1['whale']")
print(fdist1['whale'])
print("-" * 40)

print(">>> fdist2 = FreqDist(text2)")
fdist2 = FreqDist(text2)
print(">>> fdist2.most_common(50)")
print(fdist2.most_common(50))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.2  Fine-grained Selection of Words
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> V = set(text1)")
V = set(text1)
print(">>> long_words = [w for w in V if len(w) > 15]")
long_words = [w for w in V if len(w) > 15]
print(">>> sorted(long_words)")
print(sorted(long_words))
print("-" * 40)

print(">>> fdist5 = FreqDist(text5)")
fdist5 = FreqDist(text5)
print(">>> sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)")
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))
print("-" * 40)


print("""
----------------------------------------------------------------------
3.3  Collocations and Bigrams
(any key to continue)""")
raw_input()
print("-" * 40)

from nltk import bigrams
print(">>> list(bigrams['more', 'is', 'said', 'than', 'done'])")
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
print("-" * 40)

print(">>> text4.collocations()")
text4.collocations()
print(">>> text8.collocations()")
text8.collocations()
print("-" * 40)


print("""
----------------------------------------------------------------------
3.4  Counting Other Things
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> [len(w) for w in text1]")
print([len(w) for w in text1])
print(">>> fdist = FreqDist(len(w) for w in text1)")
fdist = FreqDist(len(w) for w in text1)
print(">>> print(fdist)")
print(fdist)
print(">>> fdist")
print(fdist)
print("-" * 40)

print(">>> fdist.most_common()")
print(fdist.most_common())
print(">>> fdist.max()")
print(fdist.max())
print(">>> fdist[3]")
print(fdist[3])
print(">>> fdist.freq(3)")
print(fdist.freq(3))
print("-" * 40)


print("""
----------------------------------------------------------------------
4  Back to Python: Making Decisions and Taking Control
4.1  Conditionals
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> sent7")
print(sent7)
print(">>> [w for w in sent7 if len(w) < 4]")
print([w for w in sent7 if len(w) < 4])
print(">>> [w for w in sent7 if len(w) <= 4]")
print([w for w in sent7 if len(w) <= 4])
print(">>> [w for w in sent7 if len(w) == 4]")
print([w for w in sent7 if len(w) == 4])
print(">>> [w for w in sent7 if len(w) != 4]")
print([w for w in sent7 if len(w) != 4])
print("-" * 40)

print(">>> sorted(w for w in set(text1) if w.endswith('ableness'))")
print(sorted(w for w in set(text1) if w.endswith('ableness')))
print(">>> sorted(term for term in set(text4) if 'gnt' in term)")
print(sorted(term for term in set(text4) if 'gnt' in term))
print(">>> sorted(item for item in set(text6) if item.istitle())")
print(sorted(item for item in set(text6) if item.istitle()))
print(">>> sorted(item for item in set(sent7) if item.isdigit())")
print(sorted(item for item in set(sent7) if item.isdigit()))
print("-" * 40)

print(">>> sorted(w for w in set(text7) if '-' in w and 'index' in w)")
print(sorted(w for w in set(text7) if '-' in w and 'index' in w))
print(">>> sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10)")
print(sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10))
print(">>> sorted(w for w in set(sent7) if not w.islower())")
print(sorted(w for w in set(sent7) if not w.islower()))
print(">>> sorted(t for t in set(text2) if 'cie' in t or 'cei' in t)")
print(sorted(t for t in set(text2) if 'cie' in t or 'cei' in t))
print("-" * 40)


print("""
----------------------------------------------------------------------
4.2  Operating on Every Element
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> [len(w) for w in text1]")
print([len(w) for w in text1])
print(">>> [w.upper() for w in text1]")
print([w.upper() for w in text1])
print("-" * 40)

print(">>> len(text1)")
print(len(text1))
print(">>> len(set(text1))")
print(len(set(text1)))
print(">>> len(set(word.lower() for word in text1))")
print(len(set(word.lower() for word in text1)))
print("-" * 40)

print(">>> len(set(word.lower() for word in text1 if word.isalpha()))")
print(len(set(word.lower() for word in text1 if word.isalpha())))
print("-" * 40)


print("""
----------------------------------------------------------------------
4.3  Nested Code Blocks
(any key to continue)""")
raw_input()
print("-" * 40)
print("----- skipped -----")


print("""
----------------------------------------------------------------------
4.4  Looping with Conditions
(any key to continue)""")
raw_input()
print("-" * 40)

print(">>> sent1 = ['Call', 'me', 'Ishmael', '.']")
print(">>> for xyzzy in sent1:")
print(">>>     if xyzzy.endswith('l'):")
print(">>>         print(xyzzy)")
sent1 = ['Call', 'me', 'Ishmael', '.']
for xyzzy in sent1:
    if xyzzy.endswith('l'):
        print(xyzzy)
print("-" * 40)

print(">>> for token in sent1:")
print(">>>     if token.islower():")
print(">>>         print(token, 'is a lowercase word')")
print(">>>     elif token.istitle():")
print(">>>         print(token, 'is a titlecase word')")
print(">>>     else:")
print(">>>         print(token, 'is punctuation')")
for token in sent1:
    if token.islower():
        print(token, 'is a lowercase word')
    elif token.istitle():
        print(token, 'is a titlecase word')
    else:
        print(token, 'is punctuation')
print("-" * 40)

print(">>> tricky = sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)")
print(">>> for word in tricky:")
print(">>>     print(word, end=' ')")
tricky = sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)
for word in tricky:
    print(word, end=' ')
print("")
print("-" * 40)


# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

from nltk.book import *

print("""
----------------------------------------------------------------------
4  Back to Python: Making Decisions and Taking Control
4.1  Conditionals
----------------------------------------------------------------------
""")

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
----------------------------------------------------------------------
""")

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
----------------------------------------------------------------------
""")
print("----- skipped -----")


print("""
----------------------------------------------------------------------
4.4  Looping with Conditions
----------------------------------------------------------------------
""")

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


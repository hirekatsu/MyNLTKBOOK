# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

print("""
----------------------------------------------------------------------
4  Writing Structured Programs
4.1  Back to the Basics
----------------------------------------------------------------------
""")

print("Assignment")
foo = 'Monty'
bar = foo
foo = 'Python'
print(bar)
print("-" * 40)

foo = ['Monty', 'Python']
bar = foo
foo[1] = 'Badlin'
print(bar)
print("-" * 40)

empty = []
nested = [empty, empty, empty]
print(nested)
nested[1].append('Python')
print(nested)
print("-" * 40)

nested = [[]] * 3
nested[1].append('Python')
nested[1] = ['Monty']
print(nested)
print("-" * 40)

print("Equality")
size = 5
python = ['Python']
snake_nest = [python] * size
print(snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4])
print(snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4])
print("-" * 40)

import random
position = random.choice(range(size))
snake_nest[position] = ['Python']
print(snake_nest)
print(snake_nest[0] == snake_nest[1] == snake_nest[2] == snake_nest[3] == snake_nest[4])
print(snake_nest[0] is snake_nest[1] is snake_nest[2] is snake_nest[3] is snake_nest[4])
print("-" * 40)

print([id(snake) for snake in snake_nest])
print("-" * 40)

print("Conditionals")
mixed = ['cat', '', ['dog'], []]
for element in mixed:
    if element:
        print(element)
print("-" * 40)

animals = ['cat', 'dog']
if 'cat' in animals:
    print(1)
elif 'dog' in animals:
    print(2)
print("-" * 40)

sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
print(all(len(w) > 4 for w in sent))
print(any(len(w) > 4 for w in sent))
print("-" * 40)


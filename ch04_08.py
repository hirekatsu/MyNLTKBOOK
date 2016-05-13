# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize

# from matplotlib import use
# use('Agg')

print("""
----------------------------------------------------------------------
4.8  A Sample of Python Libraries
----------------------------------------------------------------------
""")

print("Matplotlib")
from numpy import arange
from matplotlib import pyplot
colors = 'rgbcmyk'  # red, green, blue, cyan, magenta, yellow, black


def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    ind = arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pyplot.bar(ind+c*width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)
    pyplot.xticks(ind+width, words)
    pyplot.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pyplot.ylabel('Frequency')
    pyplot.title('Frequency of Six Modal Verbs by Genre')
    pyplot.show()

genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
    (genre, word) for genre in genres for word in nltk.corpus.brown.words(categories=genre))
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
bar_chart(genres, modals, counts)
print("-" * 40)

from matplotlib import use, pyplot
#use('Agg')
pyplot.savefig('modals.png')
print('Content-Type: text/html')
print()
print('<html><body>')
print('<img src="modals.png"/>')
print('</body></html>')
print("-" * 40)

print("NetworkX")
import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn


def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name, child.name)
        traverse(graph, start, child)

def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G, start, start)
    return G


def graph_draw(graph):
    nx.draw_graphviz(graph,
                     node_size=[16 * graph.degree(n) for n in graph],
                     node_color=[graph.depth[n] for n in graph],
                     with_labels=False)
    matplotlib.pyplot.show()

# dog = wn.synset('dog.n.01')
# graph = hyponym_graph(dog)
# graph_draw(graph)
# # need to install pygraphviz but some technical difficulties
print("-" * 40)

print("csv")
import csv
input_file = open('lexicon.csv', 'rb')
for row in csv.reader(input_file):
    print(row)
print("-" * 40)

print("NumPy")
from numpy import array
code = array([[[0, 0, 0], [1, 1, 1], [2, 2, 2]],
              [[3, 3, 3], [4, 4, 4], [5, 5, 5]],
              [[6, 6, 6], [7, 7, 7], [8, 8, 8]]])
print(code[1, 1, 1])
print(code[2].transpose())
print(code[2,1:])
print("-" * 40)

from numpy import linalg
a = array([[4, 0], [3, -5]])
u, s, vt = linalg.svd(a)
print(u)
print(s)
print(vt)
print("-" * 40)

print("Other Python Libraries")
print("----- no code -----")


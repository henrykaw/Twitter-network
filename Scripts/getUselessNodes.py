#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:17:29 2017

@author: henrikkawa
"""

import pandas as pd
import pickle
from os import listdir
import networkx as nx
import community

files = []

#Get list of relevant files
for file in listdir():
    if file.startswith('csv_'):
        files.append(file)
files = sorted(files)
print(files)

def checkNeighbors(node):
    remove = True
    for neighbor in G.neighbors(node):
        if (G.degree(neighbor) > 3):
            remove = False
            break
    return remove

for f in files:
    G = nx.Graph()
    count = 0
    print(f)
    df = pd.read_csv(f, names=['id1','id2','weigth'],nrows=1000000)
    print('dataframe loaded')
    for row in list(zip(df['id1'],df['id2'], df['weigth'])):
        G.add_edge(row[0], row[1], weight=row[2])
        count += 1
        if (count % 100000 ==0):
            print(count)
    print('Network created - nodes: ',len(G.nodes()))
    remove = [node for node,degree in G.degree() if degree < 3 and 
              checkNeighbors(node)]
    G.remove_nodes_from(remove)
    print('Network cleaned - nodes: ',len(G.nodes()))
    print('Saving networking to file...')
    with open('graph_'+f[4:6]+'.pickle','wb') as pickle_file:
        pickle.dump(G, pickle_file)
    print('Saving removable nodes to file...')
    with open('removable_nodes_'+f[4:6]+'.pickle','wb') as pickle_file_1:
        pickle.dump(remove,pickle_file_1)
    print('Finding communities...')
    partition = community.best_partition(G)
    print('Communites found')
    print('Saving communities to file...')
    with open('Communities_'+f[4:6]+'.pickle','wb') as pickle_file_2:
        pickle.dump(partition, pickle_file_2)
    print('Communities saved')
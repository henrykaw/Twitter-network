#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:09:12 2017

@author: henrikkawa
"""
import pickle
import networkx as nx
from os import listdir

files = []
for file in listdir():
    if file.startswith('graph_'):
        files.append(file)
files = sorted(files)
print(files)

for file in files:
    with open(file,'rb') as f:
        print('opening ', file, '...')
        G = pickle.load(f)
        print('Nodes: ',len(G.nodes()),'Links: ', len(G.edges())
        ,' Average cluster: ',nx.average_clustering(G))
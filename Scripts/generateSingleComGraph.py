#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:39:39 2017

@author: henrikkawa
"""
# pylint: disable=invalid-name
import pickle
import networkx as nx

comPath = '../communities/'
replyPath = '../usedCsv/'
f= 'Communities_01.pickle'
def loadCommunity():
    for key1 in comObj.keys():
        if comObj[key1] in community_size_dict:
            community_size_dict[comObj[key1]].append(key1)
        else:
            community_size_dict[comObj[key1]] = [key1]

    for key2 in community_size_dict.keys():
        for node in community_size_dict[key2]:
            for neighbor_node in replyDict[node]:
                neighbor_community_num = comObj[neighbor_node]
                if (neighbor_node in comObj) and (neighbor_community_num != key2):

                    if (key2 in community_link_dict) and (neighbor_community_num in community_link_dict[key2]):
                        community_link_dict[key2][neighbor_community_num] += 1

                    elif key2 in community_link_dict:
                        community_link_dict[key2][neighbor_community_num] = 1

                    else:
                        community_link_dict[key2] = {}
                        community_link_dict[key2][neighbor_community_num] = 1


                    if (neighbor_community_num in community_link_dict) and (key2 in community_link_dict[neighbor_community_num]):
                        community_link_dict[neighbor_community_num][key2] += 1

                    elif neighbor_community_num in community_link_dict:
                        community_link_dict[neighbor_community_num][key2] = 1

                    else:
                        community_link_dict[neighbor_community_num] = {}
                        community_link_dict[neighbor_community_num][key2] = 1

with open(comPath + f, 'rb') as fp, open(replyPath + 'replyDict_' + f[12:14] + '.pickle', 'rb') as fReply:
    comObj = pickle.load(fp)
    replyDict = pickle.load(fReply)

    community_size_dict = {}
    community_link_dict = {}

    loadCommunity()

    g = nx.Graph()
    community_node_size = []
    for community in sorted(community_size_dict.keys()):
        community_node_size.append(len(community_size_dict[community]))
        g.add_node(community, size=len(community_size_dict[community]))
        community_node_size_normalise = [float(i)/sum(community_node_size) for i in community_node_size]

    for comNode in sorted(community_link_dict.keys()):
        for edge in community_link_dict[comNode]:
            g.add_edge(comNode, edge, weight=community_link_dict[comNode][edge])

    edgewidth = [d['weight'] for (u, v, d) in g.edges(data=True)]
    nx.write_gexf(g, 'community_graph_' + f[12:14] + '.gexf')

print('Nodes:', len(g.nodes()), 'Links:',
    len(g.edges()), 'Average cluster:', nx.average_clustering(g))
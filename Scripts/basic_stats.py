
import pandas as pd
import networkx as nx
from collections import Counter
from os import listdir
import json
files = []
csv_dict = {}


for file in listdir():
    if file.startswith('csv_'):
        files.append(file)
        csv_dict[file]= {}


for f in files:
    print(f)
    df = pd.read_csv(f, names=['id1','id2','weigth'])
    G = nx.Graph()
    for index,row in df.iterrows():
        G.add_edge(row['id1'],row['id2'], weight=row['weigth'])
    print("Graph loaded")
    csv_dict[f]['num_nodes'] = G.number_of_nodes()
    csv_dict[f]['num_egdes'] = G.number_of_edges()
    csv_dict[f]['clustering'] = nx.average_clustering(G)
    csv_dict[f]['degree'] = dict(Counter(dict(nx.degree(G)).values()))

with open('result.json', 'w') as fp:
    json.dump(csv_dict, fp)


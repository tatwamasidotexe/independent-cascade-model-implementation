import pandas as pd
import os
import re
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
from networkx import DiGraph

df_csv_concat = pd.concat([pd.read_csv('degree1000.csv'), pd.read_csv('degree10000.csv'), pd.read_csv('degree25000.csv')], ignore_index=True)
df_csv_concat.columns = ['A', 'B']


G=nx.from_pandas_edgelist(df_csv_concat, "A", "B", create_using = DiGraph())

N=list(G.nodes)[:10000]
sub_graph = G.subgraph(N)
print(nx.is_connected(sub_graph.to_undirected()))
print(len(df_csv_concat.index))
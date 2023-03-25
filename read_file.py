import networkx as nx
import pandas as pd
import os
import re


#df1 = pd.read_csv("12831.edges", sep="\s+")
#df1.to_csv("12831.csv", index=None)

#df = pd.read_csv("12831.edges", delim_whitespace=True, names=("A", "B"))
#G=nx.from_pandas_edgelist(df, "A", "B", create_using=nx.DiGraph())
#print(len(G.nodes))
#print(len(G.edges))
results = []
results += [each for each in os.listdir('twitter') if each.endswith('.edges')]
#print(results[0])
df = pd.read_csv("twitter/"+results[0], delim_whitespace=True, names=("A", "B"))
G=nx.from_pandas_edgelist(df, "A", "B", create_using=nx.DiGraph())
print(G.edges)
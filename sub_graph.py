import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
from networkx import DiGraph

df = pd.read_csv("degree25000.csv", delim_whitespace = False, names = ("A", "B"))

G=nx.from_pandas_edgelist(df, "A", "B", create_using = DiGraph())

N=list(G.nodes)[:10000]
sub_graph = G.subgraph(N)
print(sub_graph)
#print(nx.is_connected(sub_graph.to_undirected()))
#avg_path_length = nx.average_shortest_path_length(sub_graph.to_undirected())
#print(avg_path_length)
#avg_degree = sum(val * count for val, count in nx.average_degree_connectivity(sub_graph).items())/len(sub_graph)
#print(avg_degree)
#p = avg_degree/len(sub_graph)
#print(p)

small_world = nx.watts_strogatz_graph(10000, 9970, 0.99)
print(small_world)




import networkx as nx
import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import scipy as sp
from networkx import DiGraph

results = []
results += [each for each in os.listdir('twitter') if each.endswith('.edges')]

# G stores different ego-centric graphs for every node in the dataset
G=[]
for i in results:
    df = pd.read_csv("twitter/"+i, delim_whitespace = True, names = ("A", "B"))
    G.append(nx.from_pandas_edgelist(df, "A", "B", create_using = DiGraph()))


def find_unique_nodes(graphs, num_unique):
    node_count = {}
    for graph in graphs:
        for node in graph.nodes:
            if node in node_count:
                node_count[node] += 1
            else:
                node_count[node] = 1
    unique_nodes = set()
    while len(unique_nodes) < num_unique:
        for node, count in node_count.items():
            if count == 1 and node not in unique_nodes:
                unique_nodes.add(node)
            if len(unique_nodes) == num_unique:
                break
    return unique_nodes
    
unique_nodes = find_unique_nodes(G, 10000)
nodes_list = list(unique_nodes)

def find_unique_edges(graphs):
    unique_edges = set()
    for graph in graphs:
        unique_edges.update(graph.edges)
    return unique_edges
edges_list = list(find_unique_edges(G))
master_graph = DiGraph()
master_graph.add_edges_from(edges_list)
sub_graph = master_graph.subgraph(nodes_list)
print(nx.is_strongly_connected(sub_graph))

#R=[]
#for i in G[1:]:
        # M = intersection of 
#        M = nx.intersection(G[0], i)
#        if len(M.nodes) > 0:
#            R.append(i)

#U = G[0]
#for j in R:
#    U = nx.union(U, j, rename=('X', 'Y'))

#avg_degree = sum(val * count for val, count in nx.average_degree_connectivity(U).items())/len(U)

#avg_degree = sum(dict(U.degree()).values())/float(len(U))
#print(avg_degree)
#print(nx.average_shortest_path_length(U.to_undirected()))
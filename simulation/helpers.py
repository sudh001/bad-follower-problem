import networkx as nx
import numpy as np

def find_index(G, node):
    return list(G.nodes()).index(node)

def find_next_vertex_in_sp(G, cur, end):
    if not nx.has_path(G, cur, end):
        return None
    return nx.shortest_path(G, cur, end)[1] if len(nx.shortest_path(G, cur, end)) else end 

def is_neigh(G, src, end):
    return end in G[src]

def degree(G, v):
    return len(G[v])

def prob_of_n_given_cur(G, cur, end, n, p):
    if not is_neigh(G, cur, n) or cur == end or degree(G, cur) == 0:
        return 0
    elif degree(G, cur) == 1:
        return 1 
    elif n == find_next_vertex_in_sp(G, cur, end):
        return p + (1 - p)/(degree(G, cur))
    else:
        return (1 - p)/(degree(G, cur))
    



if __name__ == "__main__":
    edges = [
        (0, 3, 1),
        (0, 1, 4),
        (0, 2, 2),
        (1, 3, 3)
    ]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    assert find_next_vertex_in_sp(G, 2, 3) == 0
    G.add_node(4)
    assert find_next_vertex_in_sp(G, 1, 4) == None 
    

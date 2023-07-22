import networkx as nx 
import numpy as np 
from helpers import find_next_vertex_in_sp
import helpers as hp
def find_index(G, node):
    return list(G.nodes()).index(node)

def compute_A(G: nx.Graph, en, p):
    num_nodes = G.number_of_nodes()
    arr = [[hp.prob_of_n_given_cur(G, cur, en, n, p) for n in range(num_nodes)] for cur in range(num_nodes)]
    return np.array(arr)

def get_adj_mat(G):
    num_nodes = G.number_of_nodes()
    arr = [[0. for _ in range(num_nodes)] for _ in range(num_nodes)]
    for v_ind, v in enumerate(G.nodes()):
        for n in G[v]:
            n_ind = find_index(G, n)
            arr[v_ind][n_ind] = G[v][n]['weight'] if 'weight' in G[v][n] else 1. 
    return np.array(arr)
    

def compute_C(G: nx.Graph, en, p):
    A = compute_A(G, en, p)
    M = get_adj_mat(G)
    
    return np.sum(A*M, axis = -1, keepdims= True)

def get_Ap(G, en, p):
    return np.array([[hp.prob_of_n_given_cur(G, i, en, j, p) for j in G.nodes()] for i in G.nodes()])
    
def get_adj_mat(G):
    num_nodes = G.number_of_nodes()
    arr = [[0. for _ in range(num_nodes)] for _ in range(num_nodes)]
    for v_ind, v in enumerate(G.nodes()):
        for n in G[v]:
            n_ind = find_index(G, n)
            arr[v_ind][n_ind] = G[v][n]['weight'] if 'weight' in G[v][n] else 1. 
    return np.array(arr)


def avg_dist_travelled_by_bad_follower(G: nx.Graph, en, p):
    Ap = get_Ap(G, en, p)
    A = get_adj_mat(G)
    E = np.linalg.inv(np.eye(len(G.nodes())) - Ap) @ np.sum(Ap*A, axis = 1, keepdims = True)
    return E





            


        
        


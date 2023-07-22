import networkx as nx 
import random as r
from math import inf 
from helpers import find_next_vertex_in_sp
import helpers as hp


def flip_with_prob(p) -> bool:
    return r.random() < p 


def bad_follower_next_vertex(G, cur, end, p):
    if not nx.has_path(G, cur, end):
        return None 

    n_in_arr = [n for n in G[cur]]
    probs = [hp.prob_of_n_given_cur(G, cur, end, n, p) for n in n_in_arr]
    cum_probs = [sum(probs[:i+1]) for i in range(len(probs))]
    rnd = r.random()
    for ind, cp in enumerate(cum_probs):
      if cp > rnd:
        return n_in_arr[ind]


def dist_travelled_by_bad_follower(G, st, end, p):
    trav = st
    length = 0 
    while trav != end:
        next = bad_follower_next_vertex(G, trav, end, p)
        if next == None:
            return inf 
        length += G[trav][next]['weight']
        trav = next 
    return length

def avg_dist_travelled_by_bad_follower(G, st, end, p, n_runs = 20):
    total = 0
    for _ in range(n_runs):
        total += dist_travelled_by_bad_follower(G, st, end, p)
    return total/n_runs





    
import networkx as nx
import bad_follower_sim as bfs
import bad_follower_formula as bf_f

edges = [
    (0, 1, 2.0),
    (1, 2, 1.2),
    (2, 3, 4.3),
    (1, 4, 1.1),
    (2, 4, 0.2)
]

# edges = [
#     (0, 1, 1.0)
# ]

def edges_to_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G 


if __name__ == "__main__":
    G = edges_to_graph(edges)
    p = 0.8
    en = 3
    st = 0
    st_ind = list(G.nodes()).index(node)
    n_sim = 200

    print(f"avg shortest_path bw {st} and {en} using formuls", bf_f.avg_dist_travelled_by_bad_follower(G, en, p)[st_ind])

    print(f"avg shortest_path avg dist bw {st} and {en} by {n_sim} simulations, ", bfs.avg_dist_travelled_by_bad_follower(G, st, en, p, n_sim))


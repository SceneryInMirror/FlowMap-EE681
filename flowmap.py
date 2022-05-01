# Topological Order
# Levelization
# Nt: fan-in cone of a node t
# Nt': collapse nodes
# Nt'': duplicate nodes with capacity 1 or infinity

from json.encoder import INFINITY
import v2networkx as v2n
import networkx as nx
import sys
import math
import matplotlib.pyplot as plt

def init_label(G):
    for n in G.nodes:
        if G.nodes[n]["type"] == 'input':
            G.nodes[n]["label"] = 0
        else:
            G.nodes[n]["label"] = -1

def construct_Nt_pp(Nt_p, t):
    # TODO
    print(nx.info(Nt_p))
    Nt_pp = Nt_p.copy()
    for e in Nt_pp.edges:
        e["capacity"] = math.inf
    for n in Nt_pp.nodes:
        if n == t:
            continue
        dup_n = n + "_dup"
        Nt_pp.add_node(dup_n, type=Nt_pp.nodes[n]["type"], label=Nt_pp.nodes[n]["label"])
        for _, out_node in Nt_pp.out_edges(n):
            Nt_pp.add_edge(dup_n, out_node, capacity=math.inf)
            Nt_pp.remove_edge(n, out_node)
        Nt_pp.add_edge(n, dup_n, capacity=1)
    Nt_pp.add_node("s", type="source", label=0)
    for n in Nt_pp.nodes:
        if Nt_pp.nodes[n]["type"] == "input":
            Nt_pp.add_edge("s", n, capacity=math.inf)
    print(nx.minimum_cut(Nt_pp, "s", t))
    print(nx.info(Nt_pp))
    nx.draw(Nt_pp, with_labels=True)
    plt.savefig("test.png")

def labeling(G):
    init_label(G)
    for n in nx.topological_sort(G):
        max_l = -1
        for pred in G.predecessors(n): # TODO: should we use predecessors, or just consider in_edges?
            max_l = max(G.nodes[pred]["label"], max_l)
        if max_l > 0: # if there are only inputs in the fan-in cone, then skip the collapsing step
            ## construct the subgraph Nt
            Nt = G.subgraph([n, G.predecessors(n)])
            print("Nt", nx.info(Nt))
            ## construct Nt'
            Nt_p = Nt.copy()
            for pred in Nt.predecessors(n):
                if Nt.nodes[pred]["label"] == max_l:
                    for in_node, _ in G.in_edges(pred):
                        Nt_p.add_edge(in_node, n)
            for pred in Nt.predecessors(n):
                if Nt.nodes[pred]["label"] == max_l:
                    Nt_p.remove_node(pred)
            ## construct Nt'', which may be not needed
            print("construct Nt for node %s", n)
            construct_Nt_pp(Nt_p, n)

        # if find K-cut:
            # G.nodes[n]["label"] = max_l
        # if cannot find K-cut:
        G.nodes[n]["label"] = max_l + 1
        

def mapping(G):
    pass

def main(argv):
    G = v2n.v2networkx(argv[1])
    v2n.remove_wires(G)
    print("v2networkx done!")
    labeling(G)


if __name__ == "__main__":
    main(sys.argv)
from json.encoder import INFINITY
from posixpath import split
import v2networkx as v2n
import networkx as nx
import sys
import math
import matplotlib.pyplot as plt


K = 6 # parameter K: the number of inputs for one LUT
INF = 10000 # parameter INF: a large enough number to represent the capacity of edges between duplicated nodes


def cust_print(str):
    print("\n", "#"*32, sep="")
    print("#", str)
    print("#"*32, "\n", sep="")


def init_label(G):
    for n in G.nodes:
        if G.nodes[n]["type"] == "input":
            G.nodes[n]["label"] = 0
        else:
            G.nodes[n]["label"] = -1


def construct_Nt_pp(Nt_p, t):
    global K
    global INF
    Nt_pp = Nt_p.copy()
    nx.set_edge_attributes(Nt_pp, [INF], "capacity") # for the edge between two different nodes, the capacity should be INF
    for n in Nt_p.nodes:
        if n == t: # do not need to duplicate the node t
            continue

        ## duplicate a node and regenerate edges
        dup_n = n + "_dup"
        Nt_pp.add_node(dup_n, type=Nt_p.nodes[n]["type"], label=Nt_p.nodes[n]["label"])
        for _, out_node in Nt_p.out_edges(n):
            Nt_pp.add_edge(dup_n, out_node, capacity=INF)
            Nt_pp.remove_edge(n, out_node)
        Nt_pp.add_edge(n, dup_n, capacity=1)

    ## create a source node
    Nt_pp.add_node("s", type="source", label=0)
    for n in Nt_pp.nodes:
        if Nt_pp.nodes[n]["type"] == "input":
            Nt_pp.add_edge("s", n, capacity=INF)
    
    ## find the minimum cut
    min_cut = nx.minimum_cut(Nt_pp, "s", t) 
    if min_cut[0] <= K:
        print("Mincut for node %s: \nMincut size: %d\nMincut clusters: %s\n" % (t, min_cut[0], min_cut[1]))

    return min_cut


def labeling(G):
    cust_print("Start labeling")
    global K
    global INF
    init_label(G) # assign 0 to inputs and -1 to other nodes as the initial label
    for n in nx.topological_sort(G):
        max_l = -1
        cut_size = INF
        for anc in nx.ancestors(G, n): # TODO: should we use predecessors, or ancestors?
            max_l = max(G.nodes[anc]["label"], max_l)
        if max_l > 0: # if there are only inputs in the fan-in cone, then skip the collapsing step
            
            ## construct the subgraph Nt
            Nt = G.subgraph([n] + [p for p in nx.ancestors(G, n)]) # ancestors are the nodes that have paths to the target, while predecessors have direct edges to the target
            
            ## construct Nt'
            Nt_p = Nt.copy()
            for anc in nx.ancestors(Nt, n):
                if Nt.nodes[anc]["label"] == max_l:
                    for in_node, _ in G.in_edges(anc):
                        Nt_p.add_edge(in_node, n)
            for anc in nx.ancestors(Nt, n):
                if Nt.nodes[anc]["label"] == max_l:
                    Nt_p.remove_node(anc)
            
            ## construct Nt'', which may be not needed
            min_cut = construct_Nt_pp(Nt_p, n)
            cut_size = min_cut[0]

        ## assign label to the node t according to the minimum cut size
        if cut_size <= K:
            G.nodes[n]["label"] = max_l
            G.nodes[n]["mincut"] = min_cut
        else:
            G.nodes[n]["label"] = max_l + 1
            G.nodes[n]["mincut"] = None

    ## print all information about nodes after labeling
    cust_print("Graph info after labeling")
    print(G.nodes.data())


def mapping(G):
    pass # TODO


def main(argv):
    G = v2n.v2networkx(argv[1]) # generate a networkx graph from the netlist, where both gates, IOs, wires are nodes
    v2n.remove_wires(G) # remove nodes that represent wires in the netlist
    cust_print("v2networkx done!")
    labeling(G) # assign label to each node
    mapping(G)


if __name__ == "__main__":
    main(sys.argv)
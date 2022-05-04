from hashlib import new
from ipaddress import collapse_addresses
from json.encoder import INFINITY
from posixpath import split
from tkinter import N
import v2networkx as v2n
import networkx as nx
import sys
import math
import matplotlib.pyplot as plt
from networkx.algorithms.flow import edmonds_karp, shortest_augmenting_path
import time


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
        Nt_pp.add_node(dup_n, type="dup", label=Nt_p.nodes[n]["label"])
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
    # min_cut = nx.minimum_cut(Nt_pp, "s", t) # TODO: we can change this function to edmonds_karp() or shortest_augmenting_path()
    min_cut = nx.minimum_cut(Nt_pp, "s", t, flow_func=edmonds_karp)
    # min_cut = nx.minimum_cut(Nt_pp, "s", t, flow_func=shortest_augmenting_path)
    # if min_cut[0] <= K:
        # print("Mincut for node %s: \nMincut size: %d\nMincut clusters: %s\n" % (t, min_cut[0], min_cut[1]))

    return min_cut


def xt_xtbar_generation(G, Nt, n, min_cut):
    if G.nodes[n]["mincut"]:
        
        ## generate Xt and Xt_bar sets for node n
        xt = min_cut[1][0].copy()
        xtbar = []
        xt.remove("s")
        for i in min_cut[1][0]:
            if ("dup" in i): xt.remove(i)
        for i in Nt.nodes:
            if (i not in xt): xtbar.append(i)
        G.nodes[n]["xt"] = xt
        G.nodes[n]["xtbar"] = xtbar

        ## cut_overlapping is used to show a node is in which nodes' cuts
        # for i in xtbar:
        #     if G.nodes(data="cut_overlapping")[i]:
        #         G.nodes[i]["cut_overlapping"] = [G.nodes[i]["cut_overlapping"]] + [n]
        #     else:
        #         G.nodes[i]["cut_overlapping"] = n

    else:
        G.nodes[n]["xtbar"] = [n]
        xt = []
        for i in Nt.nodes:
            if (i != n): xt.append(i)
        G.nodes[n]["xt"] = xt


def labeling(G):
    cust_print("Start labeling")
    global K
    global INF
    init_label(G) # assign 0 to inputs and -1 to other nodes as the initial label
    for n in nx.topological_sort(G):
        max_l = -1
        cut_size = INF
        # min_cut = None
        # Nt = None
        for anc in nx.ancestors(G, n): # TODO: should we use predecessors, or ancestors?
            max_l = max(G.nodes[anc]["label"], max_l)
        
        if max_l < 0: # for inputs
            G.nodes[n]["mincut"] = None
            G.nodes[n]["xtbar"] = [n]
            G.nodes[n]["xt"] = []

        elif max_l == 0: # if there are only inputs in the fan-in cone, then skip the collapsing step
            G.nodes[n]["label"] = 1
            G.nodes[n]["mincut"] = None
            G.nodes[n]["xtbar"] = [n]
            xt = []
            for in_node, _ in G.in_edges(n):
                xt.append(in_node)
            G.nodes[n]["xt"] = xt
            # G.nodes[n]["cut_overlapping"] = set(n)
        
        elif max_l > 0:

            ## construct the subgraph Nt
            Nt = G.subgraph([n] + [p for p in nx.ancestors(G, n)]) # ancestors are the nodes that have paths to the target, while predecessors have direct edges to the target
            
            ## construct Nt'
            Nt_p = Nt.copy()
            for anc in nx.ancestors(Nt, n):
                if Nt.nodes[anc]["label"] == max_l:
                    merge(Nt_p, n, anc)
            # for anc in nx.ancestors(Nt, n):
            #     if Nt.nodes[anc]["label"] == max_l:
            #         for in_node, _ in G.in_edges(anc):
            #             Nt_p.add_edge(in_node, n)
            # for anc in nx.ancestors(Nt, n):
            #     if Nt.nodes[anc]["label"] == max_l:
            #         Nt_p.remove_node(anc)
            
            ## construct Nt'', which may be not needed
            min_cut = construct_Nt_pp(Nt_p, n)
            cut_size = min_cut[0]

            ## assign label to the node t according to the minimum cut size
            if cut_size <= K:
                G.nodes[n]["label"] = max_l
                G.nodes[n]["mincut"] = min_cut
                xt_xtbar_generation(G, Nt, n, min_cut)
            else:
                G.nodes[n]["label"] = max_l + 1
                G.nodes[n]["mincut"] = None
                xt_xtbar_generation(G, Nt, n, min_cut)

    ## print all information about nodes after labeling
    cust_print("Graph info after labeling")


def insert_KLUT(LUT_G, G, n, mapping_list, collapse_list):
    if LUT_G.has_node(n): pass
    else:
        LUT_G.add_node(n, type="lut")
    in_nodes = []
    for i in G.nodes[n]["xtbar"]:
        # if i not in collapse_list:
            # collapse_list.append(i)
        for in_node, _ in G.in_edges(i):
            if in_node not in in_nodes and in_node not in G.nodes[n]["xtbar"]:
                in_nodes.append(in_node)
    for i in in_nodes:
        # if i in collapse_list:
            # collapse_list.remove(i)
        if i not in mapping_list and G.nodes[i]["type"] != "input":
            mapping_list.append(i)
        if LUT_G.has_node(i): pass
        elif G.nodes[i]["type"] == "input":
            LUT_G.add_node(i, type="input")
        else:
            LUT_G.add_node(i, type="lut")
        LUT_G.add_edge(i, n)


def mapping(G):
    mapping_list = []
    collapse_list = []
    LUT_G = nx.DiGraph()
    for n in G.nodes:
        if G.nodes[n]["type"] == "output":
            mapping_list.append(n) 
    while(len(mapping_list)):
        current_n = mapping_list.pop(0)
        # if (current_n in collapse_list): continue
        insert_KLUT(LUT_G, G, current_n, mapping_list, collapse_list)
        print(LUT_G.in_degree(current_n))
    return LUT_G
    

def merge(G, lut, pred):
    for in_node, _ in G.in_edges(pred):
        G.add_edge(in_node, lut)
    G.remove_node(pred)


def predecessor_packing(LUT_G):
    global K
    G = LUT_G.copy()
    LUT_GG = LUT_G.copy()

    collapsed_lut = []
    node_list = list(reversed(list(nx.topological_sort(LUT_G))))
    new_node_list = []
    while (True):
        for lut in node_list:  
            if lut in collapsed_lut: continue
            for pred, _ in LUT_GG.in_edges(lut):
                if LUT_GG.out_degree(pred) == 1 and LUT_GG.nodes[pred]["type"] != "input": # the predecessor is fanout-free
                    if G.in_degree(pred) + G.in_degree(lut) <= K:
                        # G = nx.contracted_nodes(G, lut, pred)
                        merge(G, lut, pred)
                        if lut not in new_node_list:
                            new_node_list.append(lut)
                        collapsed_lut.append(pred)


            LUT_GG = G.copy()

        node_list = new_node_list.copy()
        new_node_list.clear()
        if (len(node_list) == 0): break

    print(nx.info(LUT_GG))
    return LUT_GG


def gate_decomposition(LUT_G):
    global K
    G = LUT_G.copy()
    LUT_GG = LUT_G.copy()

    collapsed_lut = []
    node_list = list(reversed(list(nx.topological_sort(LUT_G))))
    new_node_list = []
    while (True):
        for lut in node_list:  
            if lut in collapsed_lut: continue
            for pred1, _ in LUT_GG.in_edges(lut):
                for pred2, __ in LUT_GG.in_edges(lut):
                    if (pred1 == pred2): continue
                    if (pred1 in collapsed_lut or pred2 in collapsed_lut): continue
                    if (LUT_GG.nodes[pred1]["type"] == "input" or LUT_GG.nodes[pred2]["type"] == "input"): continue
                    if ((LUT_GG.out_degree(pred1) > 1) or (LUT_GG.out_degree(pred2) > 1)): continue
                    if (G.in_degree(pred1) + G.in_degree(pred2) <= K):
                        merge(G, pred1, pred2)
                        if pred1 not in new_node_list:
                            new_node_list.append(pred1)
                        collapsed_lut.append(pred2)                        
            LUT_GG = G.copy()

        node_list = new_node_list.copy()
        new_node_list.clear()
        if (len(node_list) == 0): break
    
    print(nx.info(LUT_GG))
    return LUT_GG


def merge_LUTs(LUT_G, KLUT_n_input, i, j):
    global K
    if i + j > K:
        exit("Error!")
    collapse_lut1 = []
    collapse_lut2 = []
    for lut1 in KLUT_n_input[i]:
        for lut2 in KLUT_n_input[j]:
            if (lut1 in collapse_lut1): break
            if (lut2 in collapse_lut2): continue
            if (i == j and lut1 in collapse_lut2): break
            if (i == j and lut2 in collapse_lut1): continue
            if (lut1 == lut2): continue
            if nx.has_path(LUT_G, lut1, lut2) or nx.has_path(LUT_G, lut2, lut1): continue
            else:
                new_lut = "_".join([lut1, lut2])
                LUT_G.add_node(new_lut, type="lut2")
                for in_node, _ in LUT_G.in_edges(lut1):
                    LUT_G.add_edge(in_node, new_lut)
                for in_node, _ in LUT_G.in_edges(lut2):
                    LUT_G.add_edge(in_node, new_lut)    
                for _, out_node in LUT_G.out_edges(lut1):
                    LUT_G.add_edge(new_lut, out_node)   
                for _, out_node in LUT_G.out_edges(lut2):
                    LUT_G.add_edge(new_lut, out_node)   
                LUT_G.remove_node(lut1)
                LUT_G.remove_node(lut2)
                collapse_lut1.append(lut1)
                collapse_lut2.append(lut2)
                break
    for lut in collapse_lut1:
        KLUT_n_input[i].remove(lut)
    for lut in collapse_lut2:
        KLUT_n_input[j].remove(lut)


def KLUT_two_outputs_mapping(LUT_G):
    global K
    KLUT_n_input = {}
    KLUT_n_input[1] = []
    KLUT_n_input[2] = []
    KLUT_n_input[3] = []
    KLUT_n_input[4] = []
    KLUT_n_input[5] = []
    for lut in LUT_G.nodes:
        if LUT_G.nodes[lut]["type"] == "lut" and LUT_G.in_degree(lut) < K:
            KLUT_n_input[LUT_G.in_degree(lut)].append(lut)
    
    # This can be applied for K = 6 only
    merge_LUTs(LUT_G, KLUT_n_input, 1, 5)
    merge_LUTs(LUT_G, KLUT_n_input, 2, 4)
    merge_LUTs(LUT_G, KLUT_n_input, 3, 3)
    for m in range(4, 0, -1): 
        merge_LUTs(LUT_G, KLUT_n_input, 1, m)
    for m in range(3, 1, -1):
        merge_LUTs(LUT_G, KLUT_n_input, 2, m)
    

def test(argv):
    global K
    G = v2n.v2networkx(argv[1]) # generate a networkx graph from the netlist, where both gates, IOs, wires are nodes
    v2n.remove_wires(G) # remove nodes that represent wires in the netlist
    cust_print("v2networkx done!")
    
    labeling(G) # assign label to each node

    LUT_G = mapping(G)


def main(argv):
    global K
    G = v2n.v2networkx(argv[1]) # generate a networkx graph from the netlist, where both gates, IOs, wires are nodes
    v2n.remove_wires(G) # remove nodes that represent wires in the netlist
    cust_print("v2networkx done!")
    labeling(G) # assign label to each node
    LUT_G = mapping(G)

    # for n in G.nodes:
    #     print(n)
    #     for i in G.nodes[n]["xt"]:
    #         if (len(i) < 2): print("Error")
    #     for i in G.nodes[n]["xtbar"]:
    #         if (len(i) < 2): print("Error")
    # exit()

    # cnt = 0
    # cnt0 = 0
    # for n in LUT_G.nodes:
    #     if LUT_G.in_degree(n) < K and LUT_G.nodes[n]["type"] != "input":
    #         cnt += 1
    #     if LUT_G.in_degree(n) == 0 and LUT_G.nodes[n]["type"] != "input":
    #         print(n)
    #         cnt0 += 1
    # print(cnt, cnt0)   

    LUT_G2 = predecessor_packing(LUT_G)
    LUT_G3 = gate_decomposition(LUT_G2)

    # cnt = 0
    # cnt0 = 0
    # for n in LUT_G2.nodes:
    #     if LUT_G2.in_degree(n) < K and LUT_G2.nodes[n]["type"] != "input":
    #         cnt += 1
    #     if LUT_G2.in_degree(n) == 0 and LUT_G2.nodes[n]["type"] != "input":
    #         cnt0 += 1
    # print(cnt, cnt0)    

    LUT_G4 = predecessor_packing(LUT_G3)
    LUT_G5 = gate_decomposition(LUT_G4)
    cnt = 0
    cnt0 = 0
    for n in LUT_G5.nodes:
        if LUT_G5.in_degree(n) < K and LUT_G5.nodes[n]["type"] != "input":
            cnt += 1
        if LUT_G5.in_degree(n) == 0 and LUT_G2.nodes[n]["type"] != "input":
            cnt0 += 1
    print(cnt, cnt0)
    # LUT_GG = gate_decomposition(LUT_G)
    # LUT_GGG = predecessor_packing(LUT_GG)
    # LUT_GGG = predecessor_packing(LUT_GG)
    # LUT_GGGG = predecessor_packing(LUT_GGG)
    # postprocessing(LUT_G)

    KLUT_two_outputs_mapping(LUT_G5)
    print(nx.info(LUT_G5))
    cnt1 = 0
    cnt2 = 0
    for l in LUT_G5.nodes:
        if LUT_G5.nodes[l]["type"] == "lut2":
            cnt2 += 1
        elif LUT_G5.nodes[l]["type"] == "lut":
            cnt1 += 1
    print(cnt1, cnt2)



if __name__ == "__main__":
    # test(sys.argv)
    ts = time.time()
    main(sys.argv)
    te = time.time()
    print(te - ts)
    

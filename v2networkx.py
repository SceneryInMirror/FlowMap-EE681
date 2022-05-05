import sys
import os
import re
import networkx as nx
import matplotlib.pyplot as plt

def v2networkx(filePath):
    G = nx.DiGraph()
    # input_list = []
    # output_list = []

    f = open(filePath, "r")
    lines = (f.read()).split(";") 

    for i in range(len(lines)):
        if ("module" in lines[i]):
            continue
        lines[i] += ";"
        lines[i] = lines[i].replace("\n", " ")

        ## match input
        ## input format: each input can be any string without spaces, and current version does not support bus, for example: a, asdf456, data_0, data[0]
        if re.match(r"^(\s*)input\s+([\w\d\s,\[\]]+);$", lines[i]): 
            x = re.findall(r"[\w\d\[\]]+[,;]", lines[i]) # identify each input and store in a list x
            for j in range(len(x)):
                y = re.sub(r",|;", "", x[j]) # extract the input name
                if (y == "VDD") or (y == "GND"): # drop VDD and GND
                    continue
                G.add_node(y, type="input") # add input node into graph G
                # input_list.append(str(y))
            continue

        ## match output
        ## output format: each output can be any string without spaces, and current version does not support bus, for example: q, out456, out_0, out[0]
        if re.match(r"^(\s*)output\s+([\w\d\s,\[\]]+);$", lines[i]): 
            x = re.findall(r"[\w\d]+[,;]", lines[i]) # identify each output and store in a list x
            for j in range(len(x)):
                y = re.sub(r",|;", "", x[j]) # extract the output name
                G.add_node(y, type="output") # add output node into graph G
                # output_list.append(str(y))
            continue
        
        ## match wire
        if re.match(r"^(\s*)wire\s+([\w\d\s,\[\]]+);$", lines[i]): 
            x = re.findall(r"[\w\d\[\]]+[,;]", lines[i]) # identify each wire and store in a list x
            for j in range(len(x)):
                y = re.sub(r",|;", "", x[j]) # extract the wire name
                G.add_node(y, type="wire") # add wire node into graph G
            continue

        ## match gates
        if re.match(r"^(\s*)([\w\d]+)(\s+)([\w\d\[\]]+)(\s*)\([\w\d\s,\(\)\[\]\.]+\);$", lines[i]):
            gate = re.match(r"^\s*[\w\d]+\s+[\w\d\[\]]+", lines[i])
            gate_type = re.split(r"\s+", gate.group())[1]
            gate_name = re.split(r"\s+", gate.group())[2]
            G.add_node(gate_name,type = gate_type)
            ## for one-input gates (INV and BUF)
            if ("NOT" in gate_type) or ("BUF" in gate_type) or ("INV" in gate_type):
                ## match a port
                a = re.search(r"\.a\([\w\d\[\]]+\)", lines[i])
                if (a):
                    a_port = re.split(r"\(|\)", a.group())[1].replace(" ", "")
                    G.add_edge(a_port, gate_name)
                else:
                    exit("a port of %s doesn't exist!", gate)
                ## match O port
                O = re.search(r"\.O\([\w\d\[\]]+\)", lines[i])
                if (O):
                    O_port = re.split(r"\(|\)", O.group())[1].replace(" ", "")
                    G.add_edge(gate_name, O_port)
                else:
                    exit("O port of %s doesn't exist!", gate)
            ## for two-input gates
            else:
                ## match a port
                a = re.search(r"\.a\([\w\d\s\[\]]+\)", lines[i])
                if (a):
                    a_port = re.split(r"\(|\)", a.group())[1].replace(" ", "")
                    G.add_edge(a_port, gate_name)
                else:
                    exit("a port of %s doesn't exist!", gate)
                ## match b port
                b = re.search(r"\.b\([\w\d\s\[\]]+\)", lines[i])
                if (b):
                    b_port = re.split(r"\(|\)", b.group())[1].replace(" ", "")
                    G.add_edge(b_port, gate_name)
                else:
                    exit("b port of %s doesn't exist!", gate)
                ## match O port
                O = re.search(r"\.O\([\w\d\[\]]+\)", lines[i])
                if (O):
                    O_port = re.split(r"\(|\)", O.group())[1].replace(" ", "")
                    G.add_edge(gate_name, O_port)
                else:
                    exit("O port of %s doesn't exist!", gate)
    
    return G

def remove_wires(G):
    remove_list = []
    for n in G.nodes:
        if G.nodes[n]["type"] == "wire":
            if G.in_degree(n) > 1:
                exit("the wire %s is driven by more than one gates!", n)
            remove_list.append(n)
    for n in remove_list:
        for in_node, _ in G.in_edges(n):
            for _, out_node in G.out_edges(n):
                G.add_edge(in_node, out_node)
    G.remove_nodes_from(remove_list)

def test(argv):
    G = v2networkx(argv[1])
    print("v2networkx done!")
    # print(nx.info(G))
    remove_wires(G)
    M = nx.contracted_nodes(G, "N22", "N23")
    print(nx.info(M))
    print(M.nodes)
    print(M.edges)
    # S = {"i_2_0_13_0"}
    # T = {"o_2_0_0_0"}
    # print(nx.cut_size(G, S, T))
    # nx.draw(G, with_labels=True)
    # plt.savefig("test.png")

if __name__ == "__main__":
    test(sys.argv)

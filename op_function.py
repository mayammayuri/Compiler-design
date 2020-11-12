from op_table import *
from collections import OrderedDict
import string
from collections import deque
from tabulate import tabulate
from decimal import Decimal 
import numpy as np
import networkx as nx


def findgrp(point,grammar):
    for key in grammar.keys():
        for exp in grammar[key]:
                item_list=[]
                item_list[:0]=exp 
                for i, item in enumerate(item_list[:-1]):
                    if(item==point):
                        ith="f"+str(point)
                        jth="g"+str(point)
                        if(key==item_list[i-1]):
                            return(tuple((ith,jth)))
                        elif(key==item_list[i+1]):
                            return(tuple((jth,ith)))
def make_graph(grammar,terminals,non_terminals):
    G = nx.DiGraph() 
    tab_list=[]
    node_length=[]
    for i in terminals:
        for j in terminals:
            ith="f"+str(i)
            jth="g"+str(j)
            if (i=="x" and j=="x") or (i=="$" and j=="$"):
                print("nothing")
            elif (i=="x" and j!="x") or (i!="$" and j=="$"):
                tab_list.append(tuple((ith,jth)))
            elif (i!="x" and j=="x") or (i=="$" and j!="$"):
                tab_list.append(tuple((jth,ith)))
            elif (i==j):
                tab_list.append(findgrp(i,grammar))
            elif(i!=j):
                for x, item in enumerate(terminals[:-1]):
                    for opr in range(len(terminals)-1):
                        if(x+opr<len(terminals)):
                            if(i==item and j==terminals[x+opr]):
                                tab_list.append(tuple((jth,ith)))
                            elif(i==terminals[x+opr] and j==item):
                                tab_list.append(tuple((ith,jth)))
    G.add_edges_from(tab_list) 
    plt.figure(figsize =(9, 9)) 
    nx.draw_networkx(G, with_label = True, node_color ='green') 
    print("The longest node of the graph is",nx.algorithms.dag.dag_longest_path(G,weight='weight'))
    for i in G:
        node_length.append(nx.eccentricity(G,v=i))
        print("Each node length is ",node_length)

check_dict(grammar,terminals,non_terminals)
make_graph(grammar,terminals,non_terminals)

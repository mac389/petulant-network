# A, B, C
import pylab
import networkx as nx
import numpy as np
import random as rd

from pprint import pprint

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['text.usetex'] = True

#create the graph
#ex 0->1->2->0    1->3
T1 = nx.DiGraph()     
T1.add_edge(0,1)
T1.add_edge(1,2)
T1.add_edge(2,0)
T1.add_edge(1,3)

#set counts at each node to 0
for n in range(0, len(T1.nodes())):
    T1.add_node(n, ct =0)

#constants
ts = 10
tuple_index = 1
num_nodes = len(T1.nodes(data=True))

 
for x in range(0,ts): 
    #select starting node
    current_node= np.random.randint(low = 0, high =num_nodes, size = 1)[0]
    visited = set()
    while True:
        visited.add(current_node)
        current_count =  T1.nodes(data = True)[current_node][tuple_index]['ct']
        T1.add_node(current_node, ct = current_count+1)
        current_successors = set(T1.successors(current_node))
        valid_successors = current_successors.difference(visited)
        if not valid_successors:
            break
        current_node = rd.sample(valid_successors,1)[0]


for x in range(0,num_nodes):
    walk_count = T1.nodes(data=True)[x][tuple_index]['ct']
    print "node", x, "has been walked through", walk_count, " times "




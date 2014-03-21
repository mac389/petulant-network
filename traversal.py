import random

import networkx as nx
import numpy as np


import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['text.usetex'] = True
format =lambda text:r'\Large \textbf{%s}'%text
#create the graph
#ex 0->1->2->0    1->3
T1 = nx.DiGraph()     
T1.add_edge(0,1)
T1.add_edge(1,2)
T1.add_edge(2,0)
T1.add_edge(1,3)

iterations = 1000

flow = np.zeros((len(T1),len(T1)))
#chose starting position
current_node = np.random.randint(low=0,high=len(T1),size=1)[0]
for i in range(iterations):
	if T1.successors(current_node):
		next_node = random.choice(T1.successors(current_node))
		flow[current_node][next_node] += 1
		current_node = next_node
	else:
		current_node = random.choice(T1.nodes())
#--Visualization

flow /= float(iterations)
fig, (graph,heatmap) = plt.subplots(figsize=(8,5),nrows=1,ncols=2)
nx.draw(T1,ax=graph)
cax = heatmap.imshow(flow,interpolation='nearest',aspect='equal')
heatmap.set_xticks(range(flow.shape[1]))
heatmap.set_yticks(range(flow.shape[0]))
heatmap.set_ylabel(format('from'))
heatmap.set_xlabel(format('to'))
plt.colorbar(cax, shrink=0.65)
plt.tight_layout()
plt.show()
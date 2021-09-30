import json
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.traversal import breadth_first_search
from networkx.classes import graph
from networkx.classes.function import get_edge_attributes, get_node_attributes, number_of_nodes, subgraph
import time
import math
start_time = time.time()

# Read json file

# graph_file = open('G.json')
# graph_dictionary = json.load(graph_file)

# # Hard coded definitions
# graph_dictionary = {"1":["2","3","5"], "2":["3","4"],"3":["4","2","1"], "4":["3","2","5"], "5":["1","4"]}
# cost_dictionary = {"1,2":5, "1,3":2, "2,3":7, "2,4":1, "1,5": 15, "3,4":20, "4,5":30,
#                    "2,1":5, "3,1":2, "3,2":7, "4,2":1, "5,1": 15, "4,3":20, "5,4":30}
# distance_dictionary = {"1,2":50, "1,3":47, "2,3":120, "2,4":32, "1,5": 66, "3,4": 5, "4,5": 6,
#                        "2,1":50, "3,1":47, "3,2":120, "4,2":32, "5,1": 66, "4,3": 5, "5,4": 6}
# coord_dictionary = {"1":(0,0),"2":(2,2),"3":(2,1),"4":(5,7),"5":(1,6),}

# Opening JSON file
graph_data = open('G.json',)
graph_dictionary = json.loads(graph_data.read())

dist_data = open('Dist.json',)
distance_dictionary = json.loads(dist_data.read())

coord_data = open('Coord.json',)
coord_dictionary = json.loads(coord_data.read())

cost_data = open('Cost.json',)
cost_dictionary = json.loads(cost_data.read())

def getStraightLineDistance(node1, node2):
    """
    Takes in coordinates from 2 nodes where Node 1 = (x1,y1) and Node 2 = (x2, y2).

    Will return the straight line distance between these 2 nodes.
    """
    p1 = coord_dictionary[node1]
    p2 = coord_dictionary[node2]
    distance =math.dist(p1,p2)
    return distance

def getWeight(node1, node2, weight_dict):
    return weight_dict[f"{node1},{node2}"]


g = nx.Graph()

# Create graph
for key, value in graph_dictionary.items():
    current_node = key
    connected_nodes = value
    g.add_node(current_node, xy=coord_dictionary[current_node])
    
    for n in connected_nodes:
        g.add_node(n, xy=coord_dictionary[n])
        g.add_edge(current_node,n)
        cost_key = current_node+","+n
        # g[current_node][n]['cost'] = cost_dictionary[cost_key]
        g[current_node][n]['distance'] = distance_dictionary[cost_key]
        # if cost_key in cost_dictionary:
        #     g[current_node][n]['cost'] = cost_dictionary[cost_key]
        #     g[current_node][n]['distance'] = distance_dictionary[cost_key]

## Shortest Path

print("Shortest Path")
# path = nx.shortest_path(g, "1", "50", weight="distance")
# Does not have energy constraint checking
path = nx.astar_path(g, "1", "30", heuristic=getStraightLineDistance, weight='distance')
path_length = nx.astar_path_length(g, "1", "30", heuristic=getStraightLineDistance, weight='distance')
# print("Shortest path: " + "->".join(path))
print(path)
print("Shortest distance" + str(path_length))



# Option to subgraph
# g = subgraph(g, [str(i) for i in range(1,100)])

# # Plot and draw
# pos = nx.spring_layout(g)
# nx.draw(g, pos, with_labels=True)

# c_label = nx.get_edge_attributes(g, 'cost')
# d_label = nx.get_edge_attributes(g, 'distance')
# edge_label = {}
# for edge, cost in c_label.items():
#     edge_label[edge] = f"({d_label[edge]},{cost})"

# distance_label = nx.get_edge_attributes(g,'distance')
# # nx.draw_networkx_edge_labels(g, pos, edge_labels=distance_label)
# nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_label)


# # coord_label = nx.get_node_attributes(g, 'xy')
# # pos_attrs = {}
# # for node, coords in pos.items():
# #     pos_attrs[node] = (coords[0], coords[1] + 0.05)
# # node_attrs = nx.get_node_attributes(g, 'xy')
# # nx.draw_networkx_labels(g, pos_attrs, labels=node_attrs)
# path = nx.shortest_path(g, "3", "5", weight="cost")
# print(path)

# plt.show()





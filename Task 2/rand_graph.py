import networkx as nx
import matplotlib.pyplot as plt
import random
import json
import networkx.algorithms.isomorphism as iso


nodeNum = int(input("Number of nodes: "))

G = nx.fast_gnp_random_graph(nodeNum, 0.9, seed=None, directed=False)

print(f"Number of edges: {len(G.edges)}")

G_dict = {}
Cost_dict = {}
G_test = open("G_test.json", "w")
Cost_test = open("Cost_test.json", "w")

# for node in G.nodes():
for (u,v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(1,20)
    weight = G.edges[u,v]['weight']
    G.edges[v,u]['weight'] = weight
    edge1 = str(u) + "," + str(v)
    edge2 = str(v) + "," + str(u)
    Cost_dict[edge1] = weight
    Cost_dict[edge2] = weight
    
    # print(f"{u,v}, {G.edges[u,v]['weight']}")
    # print(f"{v,u}, {G.edges[v,u]['weight']}")

for node in G.nodes():
    e = []
    for (u,v) in G.edges():
        if node == u:
            e.append(str(v))
            G_dict[str(u)] = e
        if node == v:
            e.append(str(u))
            G_dict[str(v)] = e

G_json = json.dumps(G_dict)
G_test.write(G_json)
Cost_json = json.dumps(Cost_dict)
Cost_test.write(Cost_json)

G_test.close()
Cost_test.close()

# weight_labels = nx.get_edge_attributes(G, 'weight')    
# print(weight_labels)
pos = nx.circular_layout(G)
nx.draw(G, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)

plt.show()

'''
GRAPH = json.load(open("G.json", "r"))
COST = json.load(open("Cost.json", "r"))
DIST = json.load(open("Dist.json", "r"))

# GRAPH = json.load(open("G_test.json", "r"))
# COST = json.load(open("Cost_test.json", "r"))

TARGET = "50"
SOURCE = "1"
ENERGY_CONSTRAINT = 287932

G1 = nx.Graph(GRAPH)
# print(f"Isomorphic? {nx.is_isomorphic(G, G1)}")

for (u,v) in G1.edges():
    edge1 = str(u) + "," + str(v)
    edge2 = str(v) + "," + str(u)

    # G1.edges[u,v]['weight'] = COST[edge1]
    # G1.edges[v,u]['weight'] = COST[edge2]
    G1.edges[u,v]['weight'] = DIST[edge1]
    G1.edges[v,u]['weight'] = DIST[edge2]

    # print(f"edge1 {edge1}")
    # print(f"COST {COST[edge1]}")
    # print(f"edge2 {edge2}")
    # print(f"COST {COST[edge2]}")

shortest_path = nx.dijkstra_path(G1, source="1", target="50", weight='weight')
print(shortest_path)

# em = iso.numerical_edge_match("weight", 1)
# print(f"Isomorphic? {nx.is_isomorphic(G, G1, edge_match=em)}")

# weight_labels1 = {(u,v): G1.edges[u,v]['weight'] for (u,v) in G1.edges}

# pos1 = nx.circular_layout(G1)
# nx.draw(G1, with_labels=True)
# nx.draw_networkx_edge_labels(G1, pos1, edge_labels=weight_labels1)

# plt.show()
'''
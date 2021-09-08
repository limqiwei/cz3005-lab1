import networkx as nx
import matplotlib.pyplot as plt
import random
import json
# from networkx.readwrite import json_graph


nodeNum = int(input("Number of nodes: "))

ug = nx.fast_gnp_random_graph(nodeNum, 0.9, seed=None, directed=False)

# print("Nodes of graph: ")
# print(ug.nodes())
# print("Edges of graph: ")
# print(ug.edges())
# print("")
print("Number of edges: " + str(len(ug.edges)))

G = {}
Cost = {}
f1 = open("G_test.json", "w")
f2 = open("Cost_test.json", "w")

for node in ug.nodes():
    e = []
    for (u,v) in ug.edges():
        ug.edges[u,v]['weight'] = random.randint(1,20)
        weight = ug.edges[u,v]['weight']
        ug.edges[v, u]['weight'] = weight

        if node == u:
            e.append(str(v))
            G[str(u)] = e
            edge1 = str(u) + "," + str(v)
            edge2 = str(v) + "," + str(u)
            Cost[edge1] = weight
            Cost[edge2] = weight
        if node == v:
            e.append(str(u))
            G[str(v)] = e

# print(G)
# print(Cost)

G_json = json.dumps(G)
f1.write(G_json)
Cost_json = json.dumps(Cost)
f2.write(Cost_json)

f1.close()
f2.close()

nx.draw(ug, with_labels=True)

plt.show()


import networkx as nx
import json
import task2


GRAPH = json.load(open("G.json", "r"))
COST = json.load(open("Cost.json", "r"))
DIST = json.load(open("Dist.json", "r"))

SOURCE = "1"
TARGET = "50"
ENERGY_CONSTRAINT = 287932

G = nx.Graph(GRAPH)

for (u,v) in G.edges():
    edge1 = str(u) + "," + str(v)
    edge2 = str(v) + "," + str(u)

    G.edges[u,v]['weight'] = DIST[edge1]
    G.edges[v,u]['weight'] = DIST[edge2]

    # G.edges[u,v]['weight'] = COST[edge1]
    # G.edges[v,u]['weight'] = COST[edge2]

try:
    shortest_path = nx.dijkstra_path(G, source=SOURCE, target=TARGET, weight='weight')
    print("Shortest path:")
    print(shortest_path)
except nx.NodeNotFound:
    print("SOURCE not in G")
except nx.NetworkXNoPath:
    print("no path exists between SOURCE and TARGET")

path1 = set(shortest_path)
# print(path1)
path2 = set(task2.path_list)
# print(path2)

if path1 == path2:
    print("path has the shortest distance")
else:
    print("path does not have the shortest distance")

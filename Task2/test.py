import networkx as nx
import json
import task2


GRAPH = json.load(open("G.json", "r"))
COST = json.load(open("Cost.json", "r"))
DIST = json.load(open("Dist.json", "r"))

SOURCE = "1"
TARGET = "50"
# assume no energy constraint in task2
ENERGY_CONSTRAINT = float("inf")


if SOURCE in GRAPH and TARGET in GRAPH:
    path, _, _ = task2.UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    if path:
        path_str = list(path.split(" -> "))
        path_list = list(map(str, path_str))
        t2_path = set(path_list)
    else:
        t2_path = set()
        print("No path exists between SOURCE and TARGET!")
else:
    print("SOURCE/TARGET not in GRAPH!")


G = nx.Graph(GRAPH)

for (u,v) in G.edges():
    edge1 = str(u) + "," + str(v)
    edge2 = str(v) + "," + str(u)

    G.edges[u,v]['weight'] = DIST[edge1]
    G.edges[v,u]['weight'] = DIST[edge2]


try:
    shortest_path = nx.dijkstra_path(G, source=SOURCE, target=TARGET, weight='weight')
    # print("Shortest path:")
    # print(shortest_path)

    nx_path = set(shortest_path)

    if nx_path == t2_path:
        print("\nPath has the shortest distance\n")
    else:
        print("\nPath does not have the shortest distance\n")


except nx.NodeNotFound:
    print("SOURCE not in G")
except nx.NetworkXNoPath:
    print("No path exists between SOURCE and TARGET")
    
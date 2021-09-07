import json


def  BFS(target, source, graph, cost):
    visited = []
    queue = [[source]]

    # adj_nodes = graph[source][1], graph[source][2]
    # print(adj_nodes)

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            adj_nodes = graph[source][1], graph[source][2]
            for adj in adj_nodes:
                shortest_path = list(path)
                shortest_path.append(adj)
                queue.append(shortest_path)
                print(queue)
                if adj == target:
                    return shortest_path
        visited.append(node)


print("running...")

total_nodes = 264346
graph = json.load(open("G.json", "r"))
cost = json.load(open("Cost.json", "r"))
dist = json.load(open("Dist.json", "r"))

target = "50"
source = "1"

# for d in range(total_nodes):
    # shortest_path = BFS(target, source, graph, cost)
# print(shortest_path)


print("terminating...")


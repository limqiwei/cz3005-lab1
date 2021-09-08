import json
from queue import PriorityQueue
import time

'''
output format:
Shortest path: S->1->T.
Shortest distance: 12.
Total energy cost: 10.

total energy cost <= 287932
start node = "1"
end node = "50"
'''

def neighbours(node, graph):
    return graph[node]


def get_cost(from_node, to_node, cost):
    edge = str(from_node) + "," + str(to_node)
    return cost[edge]


def get_dist(from_node, to_node, dist):
    edge = str(from_node) + "," + str(to_node)
    return dist[edge]


def UCS(source, target, graph, cost):
    queue = PriorityQueue()
    visited = {}
    
    queue.put(source, 0)
    visited[source] = None
    prev_cost = 0

    while queue:
        current = queue.get()
        if current == target:
            break
        for next in neighbours(current, graph):
            current_cost = get_cost(current, next, cost)
            new_cost = prev_cost + current_cost
            if next not in visited or new_cost < prev_cost:
                prev_cost = new_cost
                queue.put(next, current_cost)
                visited[next] = current

    return visited


def get_path(source, target, visited, cost, dist):
    path = []
    current = target
    total_cost = 0
    total_dist = 0
    path_str = ""

    while current != source:
        path.append(int(current))
        total_cost += get_cost(current, visited[current], cost)
        total_dist += get_dist(current, visited[current], dist)
        current = visited[current]
    
    path.append(int(source))
    path.reverse()

    for node in range(len(path)-1):
        path_str += str(path[node]) + " -> "
    
    path_str += target

    return path_str, total_cost, total_dist


if __name__ == "__main__":
    print("running...")

    print("loading files...")
    graph = json.load(open("G.json", "r"))
    cost = json.load(open("Cost.json", "r"))
    dist = json.load(open("Dist.json", "r"))
    target = "50"
    source = "1"

    # graph = json.load(open("G_test.json", "r"))
    # cost = json.load(open("Cost_test.json", "r"))
    # target = "3"
    # source = "0"

    print("searching...")
    start_time = time.time()

    visited = UCS(source, target, graph, cost)
    path, total_cost, total_dist = get_path(source, target, visited, cost, dist)

    end_time = time.time()

    print("")
    print("Shortest path: " + str(path))
    print("")
    print("Shortest distance: " + str(total_dist))
    print("Total energy cost: " + str(total_cost))
    print("")

    time_taken = str(end_time - start_time)
    print("time taken: "+ time_taken + " sec")
    print("terminating...")


import json
from queue import PriorityQueue
import time

'''
The output of your algorithm should be formatted as the following:
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
    node_pair = str(from_node) + "," + str(to_node)
    return cost[node_pair]


def UCS(source, target, graph, cost):
    queue = PriorityQueue()
    visited = {}
    
    queue.put(source, 0)
    visited[source] = None
    prev_cost = 0;

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


def get_path(source, target, visited, cost):
    path = []
    total_cost = 0
    current = target
    path_format = ""

    while current != source:
        path.append(int(current))
        total_cost += get_cost(current, visited[current], cost)
        current = visited[current]
    
    path.append(int(source))
    path.reverse()

    for node in range(len(path)-1):
        path_format += str(path[node]) + " -> "
    
    path_format += target

    return path_format, total_cost


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
    path, total_cost = get_path(source, target, visited, cost)

    end_time = time.time()
    
    print("Shortest path: " + str(path))
    # print("Shortest distance: " + )
    print("Total energy cost: " + str(total_cost))

    time_taken = str(end_time - start_time)
    print("time taken: "+ time_taken + " sec")
    print("terminating...")


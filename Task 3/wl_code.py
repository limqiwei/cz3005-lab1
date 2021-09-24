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
    cost_data = {} # "3" : "10" => Total cost from the source node

    # queue.put(source, 0)
    queue.put((0, source))
    visited[source] = None
    cost_data[source] = 0

    # prev_cost = 0

    while queue:
        # current = queue.get()
        (curr_cost, current) = queue.get()
        print(current)
        if current == target:
            break
        for next in neighbours(current, graph):
            current_cost = get_cost(current, next, cost)
            new_cost = cost_data[current] + current_cost
            # new_cost = prev_cost + current_cost
            # print(next)
            # print(f"Previous Cost: {prev_cost}, New cost: {new_cost}")
            if (next not in visited and new_cost < 287932): # new_cost < prev_cost and new_cost < 287932
                cost_data[next] = new_cost
                # queue.put(next, current_cost)
                queue.put((current_cost, next))
                visited[next] = current

    return visited


def get_path(source, target, visited, cost, dist):
# def get_path(source, target, visited, cost):
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
    
    # path_str += target
    path_str += str(path[node+1])

    return path_str, total_cost, total_dist
    # return path_str, total_cost


def main():
    print("running...")

    print("loading files...")
    graph = json.load(open("G.json", "r"))
    cost = json.load(open("Cost.json", "r"))
    dist = json.load(open("Dist.json", "r"))
    # target = "50"
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
    # path, total_cost = get_path(source, target, visited, cost)

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


if __name__ == "__main__":
    main()
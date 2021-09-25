import json
from queue import PriorityQueue
import time


def neighbours(node, graph):
    return graph[node]


def get_cost(from_node, to_node, cost):
    edge = str(from_node) + "," + str(to_node)
    return cost[edge]


def get_dist(from_node, to_node, dist):
    edge = str(from_node) + "," + str(to_node)
    return dist[edge]


def UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY):
    queue = PriorityQueue()
    visited = {}
    dist_so_far = {}
    cost_so_far = {}

    queue.put((0, SOURCE))
    visited[SOURCE] = None
    dist_so_far[SOURCE] = 0
    cost_so_far[SOURCE] = 0

    while queue:
        current = queue.get()[1]

        if current == TARGET:
            break
 
        for next in neighbours(current, GRAPH):
            next_cost = get_cost(current, next, COST)
            new_cost = cost_so_far[current] + next_cost

            distance_to_next = get_dist(current, next, DIST) 
            new_dist = dist_so_far[current] + distance_to_next

            if next not in visited or new_dist < dist_so_far[next]:
                # if new_cost <= ENERGY:
                dist_so_far[next] = new_dist
                cost_so_far[next] = new_cost
                queue.put((new_dist, next))
                visited[next] = current

    return visited


def get_path(SOURCE, TARGET, visited, COST, DIST):
    path = []
    current = TARGET
    total_cost = 0
    total_dist = 0
    path_str = ""

    while current != SOURCE:
        path.append(int(current))
        total_cost += get_cost(current, visited[current], COST)
        total_dist += get_dist(current, visited[current], DIST)
        current = visited[current]
    
    path.append(int(SOURCE))
    path.reverse()

    for node in range(len(path)-1):
        path_str += str(path[node]) + " -> "
    
    path_str += str(path[node+1])

    global path_list 
    path_list = list(map(str, path))

    return path_str, total_cost, total_dist


# remove function before submission
def search():
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))
    TARGET = "50"
    SOURCE = "1"
    ENERGY_CONSTRAINT = 287932

    visited = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    get_path(SOURCE, TARGET, visited, COST, DIST)
    

def main():
    print("running...")

    print("loading files...")
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))
    TARGET = "50"
    SOURCE = "1"
    ENERGY_CONSTRAINT = 287932

    # # graph = json.load(open("G_test.json", "r"))
    # # cost = json.load(open("Cost_test.json", "r"))
    # # target = "3"
    # # source = "0"

    print("searching...")
    start_time = time.time()

    visited = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    path, total_cost, total_dist = get_path(SOURCE, TARGET, visited, COST, DIST)

    end_time = time.time()

    print("")
    print(f"Shortest path: {path}")
    print("")
    print(f"Shortest distance: {total_dist}")
    print(f"Total energy cost: {total_cost}")
    print("")

    time_taken = end_time - start_time
    print(f"Time taken: {time_taken} sec \n")


if __name__ == "__main__":
    main()

# remove before submission
else:
    search()


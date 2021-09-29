import json
import queue as q
import time


def neighbours(node, GRAPH):
    return GRAPH[node]


def get_cost(from_node, to_node, COST):
    edge = str(from_node) + "," + str(to_node)
    return COST[edge]


def get_dist(from_node, to_node, DIST):
    edge = str(from_node) + "," + str(to_node)
    return DIST[edge]


def UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY):
    queue = q.PriorityQueue()
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
                if new_cost <= ENERGY: # remove this to check if path has shortest dist (without energy constraint)
                    dist_so_far[next] = new_dist
                    cost_so_far[next] = new_cost
                    queue.put((new_dist, next))
                    visited[next] = current

    return visited, dist_so_far[current], cost_so_far[current]


def get_path(SOURCE, TARGET, visited):
    current = TARGET
    path = []
    path_str = ""

    while current != SOURCE:
        path.append(current)
        current = visited[current]
    
    path.append(SOURCE)
    path.reverse()

    for node in range(len(path)-1):
        path_str += path[node] + " -> "
    
    path_str += path[node+1]

    # remove before submission
    global path_list 
    path_list = list(map(str, path))

    return path_str


# remove function before submission
def search():
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))
    TARGET = "50"
    SOURCE = "1"
    ENERGY_CONSTRAINT = 287932

    visited, _, _ = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    get_path(SOURCE, TARGET, visited)
    

def main():
    print("running...")

    print("loading files...")
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))
    TARGET = "50"
    SOURCE = "1"
    ENERGY_CONSTRAINT = 287932

    # remove before submission
    # graph = json.load(open("G_test.json", "r"))
    # cost = json.load(open("Cost_test.json", "r"))
    # target = "3"
    # source = "0"

    print("searching...")
    start_time = time.time()

    visited, total_dist, total_cost = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    path = get_path(SOURCE, TARGET, visited)

    end_time = time.time()

    print("")
    print(f"Shortest path: {path}")
    print("")
    print(f"Shortest distance: {total_dist}")
    print(f"Total energy cost: {total_cost}")
    print("")

    time_taken = end_time - start_time
    print(f"Time taken: {time_taken} sec \n")


# remove before submission
if __name__ == "__main__":
    main()
else:
    search()


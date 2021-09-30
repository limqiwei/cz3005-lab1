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
    target_reached = False

    queue.put((0, SOURCE))
    visited[SOURCE] = None
    dist_so_far[SOURCE] = 0
    cost_so_far[SOURCE] = 0

    while not queue.empty():
        current = queue.get()[1]

        if current == TARGET:
            target_reached = True
            break
 
        for next in neighbours(current, GRAPH):
            next_cost = get_cost(current, next, COST)
            new_cost = cost_so_far[current] + next_cost

            distance_to_next = get_dist(current, next, DIST) 
            new_dist = dist_so_far[current] + distance_to_next

            if next not in visited or new_dist < dist_so_far[next]:
                if new_cost <= ENERGY:
                    dist_so_far[next] = new_dist
                    cost_so_far[next] = new_cost
                    queue.put((new_dist, next))
                    visited[next] = current

    return visited, dist_so_far[current], cost_so_far[current], target_reached


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

    return path_str


def search(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT):       
    print("searching...")
    start_time = time.time()

    visited, total_dist, total_cost, target_reached = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    
    end_time = time.time()

    if target_reached:
        path = get_path(SOURCE, TARGET, visited)
        print(f"\nShortest path: {path}")
        print(f"\nShortest distance: {total_dist}")
        print(f"Total energy cost: {total_cost}\n")
    else:
        print(f"\nNo path exists between SOURCE and TARGET with energy budget = {ENERGY_CONSTRAINT}.")

    time_taken = end_time - start_time
    print(f"Time taken: {time_taken} sec \n")


def custom():
    print("running...\n")

    print("loading files...")
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))

    print("")
    SOURCE = str(input("Enter source node: ")) # 1
    TARGET = str(input("Enter target node: ")) # 20
    ENERGY_CONSTRAINT = int(input("Enter energy budget: "))
    print("")

    if SOURCE in GRAPH and TARGET in GRAPH:
        search(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    else:
        print("SOURCE/TARGET not in GRAPH!")


def main():
    print("running...")

    print("loading files...\n")
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))

    SOURCE = "1"
    TARGET = "50"
    ENERGY_CONSTRAINT = 287932

    if SOURCE in GRAPH and TARGET in GRAPH:
        search(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    else:
        print("SOURCE/TARGET not in GRAPH!")
        

if __name__ == "__main__":
    main()

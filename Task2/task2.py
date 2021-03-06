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
    previousNode_recorded = {}
    dist_so_far = {}
    cost_so_far = {}
    path = ""
    
    queue.put((0, SOURCE))
    previousNode_recorded[SOURCE] = None
    dist_so_far[SOURCE] = 0
    cost_so_far[SOURCE] = 0

    while not queue.empty():
        current = queue.get()[1]

        if current == TARGET:
            path = get_path(SOURCE, TARGET, previousNode_recorded)
            break
 
        for next in neighbours(current, GRAPH):
            next_cost = get_cost(current, next, COST)
            new_cost = cost_so_far[current] + next_cost

            distance_to_next = get_dist(current, next, DIST) 
            new_dist = dist_so_far[current] + distance_to_next

            if next not in previousNode_recorded or new_dist < dist_so_far[next]:
                if new_cost <= ENERGY:
                    dist_so_far[next] = new_dist
                    cost_so_far[next] = new_cost
                    previousNode_recorded[next] = current
                    queue.put((new_dist, next))

    return path, dist_so_far[current], cost_so_far[current]


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

    path, total_dist, total_cost = UCS(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    
    end_time = time.time()

    if path:
        print(f"\nShortest path: {path}")
        print(f"\nShortest distance: {total_dist}")
        print(f"Total energy cost: {total_cost}\n")
    else:
        print(f"\nNo path exists between SOURCE and TARGET with energy budget = {ENERGY_CONSTRAINT}.")

    time_taken = end_time - start_time
    print(f"Search time: {time_taken} sec \n")


def load_files():
    print("running...")

    print("loading files...\n")
    GRAPH = json.load(open("G.json", "r"))
    COST = json.load(open("Cost.json", "r"))
    DIST = json.load(open("Dist.json", "r"))

    return GRAPH, COST, DIST


def custom():
    print("======= Start of UCS Search (Manual) =======")
    GRAPH, COST, DIST = load_files()

    # Define parameters by user input
    SOURCE = None
    TARGET = None
    ENERGY_CONSTRAINT = None

    while True:
        start = input("Enter start node: ")
        if (start not in GRAPH.keys()):
            print("Start Node does not exist. Please enter a valid start node. Try again")
        else:
            SOURCE = start
            break
    
    while True:
        end = input("Enter end node: ")
        if (end not in GRAPH.keys()):
            print("End Node does not exist. Please enter a valid start node. Try again")
        else:
            TARGET = end
            break

    while True:
        try:
            budget = int(input("Enter energy budget (integer values): "))
            ENERGY_CONSTRAINT = budget
            break
        except:
            print("Please enter only integer values.")

    print("")

    search(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    print("======= End of UCS Search (Manual) =======\n")


def main():
    print("======= Start of UCS Search (Preset) =======")
    GRAPH, COST, DIST = load_files()

    SOURCE = "1"
    TARGET = "50"
    ENERGY_CONSTRAINT = 287932
    
    search(SOURCE, TARGET, GRAPH, COST, DIST, ENERGY_CONSTRAINT)
    print("======= End of UCS Search (Preset) =======\n")


if __name__ == "__main__":
    main()
    custom()

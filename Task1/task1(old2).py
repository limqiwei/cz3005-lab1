import json
from queue import PriorityQueue
import time


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        
    def dijkstra(self, source_vertex, target_vertex, graphData, distData):
        visited = set()
        distance = {source_vertex: 0}
        parent_vertex = {source_vertex: None}

        pq = PriorityQueue()
        pq.put((0, source_vertex))

        while not pq.empty():
            (_, current_vertex) = pq.get()
            
            if current_vertex in visited:
                continue      
            
            visited.add(current_vertex)
            if current_vertex == target_vertex:
                break

            for neighbor in graphData.get(str(current_vertex)):
                    old_cost = distance.get(neighbor, float('inf'))
                    new_cost = distance[current_vertex] + distData[str(current_vertex) + "," + str(neighbor)]
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distance[neighbor] = new_cost
                        parent_vertex[neighbor] = current_vertex
        
        if target_vertex not in parent_vertex.keys():
            return None
        else:
            print("Shortest distance: " + str(distance[target_vertex]))
            return parent_vertex
    
    def goal_path(self, parent, target_vertex):
        v = target_vertex
        path_array = []
        while v is not None: # root has null parent
            path_array.append(v)
            v = parent[v]
        return path_array[::-1]



def main():
    #Open files and read into dictionary variable
    with open ('Dist.json','r') as dist_dictionary:
        distData = json.load(dist_dictionary)

    with open ('G.json','r') as graph_dictionary:
        graphData = json.load(graph_dictionary)
        
    #Close files
    dist_dictionary.close()
    graph_dictionary.close()

    #Define parameter for algorithm
    SOURCE_NODE = '1'
    TARGET_NODE = '50'
    
    #Running algorithm
    print("==== Start of Shortest Path Search - Without energy constaint (Preset) ====")
    print(f"Start node : {SOURCE_NODE}, End node: {TARGET_NODE}" + "\n")
    
    g = Graph(264346)
    start_time = time.time()

    parent = g.dijkstra(SOURCE_NODE,TARGET_NODE, graphData, distData)
    if parent != None:
        path = g.goal_path(parent,TARGET_NODE)
        print("Shortest Path: " + " -> ".join(path) + "\n")
        print("Time taken:\t%s seconds" % (time.time() - start_time))
        print("==== End of Shortest Path Search - Without energy constaint (Present) ====")
    else:
        print(f"No path exists between node {SOURCE_NODE} and node {TARGET_NODE}.")
        print("==== End of Shortest Path Search - Without energy constaint (Present) ====")
    
def custom():
    
    #Open files and read into dictionary variable
    with open ('Dist.json','r') as dist_dictionary:
        distData = json.load(dist_dictionary)

    with open ('G.json','r') as graph_dictionary:
        graphData = json.load(graph_dictionary)
    
    #Close files
    dist_dictionary.close()
    graph_dictionary.close()
    
    #Check if user input valid parameteres
    while True:
        SOURCE_NODE = str(input("Enter source node: "))
        if SOURCE_NODE not in graphData.keys():
            print("The node entered does not exist. Please enter a number between 1 to 264346.")
        else:
            break
        
    while True:
        TARGET_NODE = str(input("Enter target node: "))
        if TARGET_NODE not in graphData.keys():
            print("The node entered does not exist. Please enter a number between 1 to 264346.")
        else:
            break            
            
    #Running algorithm
    print("==== Start of Shortest Path Search - Without energy constaint (Custom) ====")
    print(f"Start node : {SOURCE_NODE}, End node: {TARGET_NODE}" + "\n")
    
    g = Graph(264346)
    start_time = time.time()

    parent = g.dijkstra(SOURCE_NODE,TARGET_NODE, graphData, distData)
    if parent != None:
        path = g.goal_path(parent,TARGET_NODE)
        print("Shortest Path: " + " -> ".join(path) + "\n")
        print("Time taken:\t%s seconds" % (time.time() - start_time))
        print("==== End of Shortest Path Search - Without energy constaint (Custom) ====")
    else:
        print(f"No path exists between node {SOURCE_NODE} and node {TARGET_NODE}.")
        print("==== End of Shortest Path Search - Without energy constaint (Present) ====")



if __name__ == "__main__":
    #main()
    custom()
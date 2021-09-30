import json
import math
from queue import PriorityQueue
import time

"""
Task 3 Problem Description

- Crate A* Search Algorith
- Source Node: 1
- Target Node: 50
- Energy Budget: 287932

A* Algorithm = Path Cost Function g(n) + Heuristic Function h(n)
Make-up of Path Cost Function: UCS
Make-up of Heuristic Function: Straight line distance to target.
"""
   
class Graph():

    class Node():
        def __init__(self, node_name, cooordinates, parent_node, g_value, total_cost, add_to_frontier_before):
            self.node_name = node_name
            self.coordinates = cooordinates
            self.parent_node = parent_node
            self.g_value = g_value #cumulative
            self.total_cost = total_cost #cumulative
            self.add_to_frontier_before = add_to_frontier_before

    def get_h_cost(self, current_coord, target_coord):
        #[x,y] [x1,y1]
        # Heuristic Cost based on distance
        distance = math.dist(current_coord,target_coord)
        return distance

    def shortest_path_ASTAR(self, source, target, graph_dict, coord_dict, cost_dict, dist_dict, energy_budget):
        node_data = {}
        for key in graph_dict.keys():
            node = self.Node(node_name=key, 
                        cooordinates=coord_dict[key],
                        parent_node=None, 
                        g_value=(-1),
                        total_cost=(-1),
                        add_to_frontier_before=False)
            node_data[key] = node

        source_node = node_data[source] # Get node object for source
        target_node = node_data[target] # Get node object for target
        target_coord =  target_node.coordinates # Get target_coordinates for future multiple calculatations of h(n)
        
        priority_queue = PriorityQueue() # This is a priority queue, using f(n), where f(n) = g(n) + h(n) 
        dummy_count = 0
        priority_queue.put((0,dummy_count, source_node))
        dummy_count += 1
    
        # Set initial settings for source node
        source_node.g_value = 0
        source_node.total_cost = 0

        # Flag to return to tell if shortest path succeeded or not
        target_reached = False
        print("Starting ASTAR Search")
        
        while(priority_queue): # While there is still things in the queue. If not then that means there is no path to the target.

            _, __, current_node = priority_queue.get()    # Get next node

            # Exploration Phase
            if (current_node.node_name == target_node.node_name): # Check if it is target
                target_reached  = True
                break # Exit loop as target is found
            else: 
                # Adding neighbours to frontier (priority queue)       
                
                # We will compute 2 values: g(n) and h(n), where n is the next node
                # g(n) : Distance from source node to this node
                # h(n) : Straight Line Distance from this node to target node (heuristically)
                # f(n) : final evalutative function being f(n) = g(n) + h(n)
                               
                current_g = current_node.g_value
                current_cost = current_node.total_cost

                neighbour_nodes = graph_dict[current_node.node_name] # return a list of neighbour nodes
                for node in neighbour_nodes:
                    neighbour_node = node_data[node]

                    next_g_value = current_g + dist_dict[f"{current_node.node_name},{neighbour_node.node_name}"]
                    next_total_cost = current_cost + cost_dict[f"{current_node.node_name},{neighbour_node.node_name}"]
                    f_cost = next_g_value + self.get_h_cost(neighbour_node.coordinates, target_coord)

                    if (neighbour_node.add_to_frontier_before):
                        # Need to check if the path is shorter or not so as to decide if want to update
                        if (next_g_value < neighbour_node.g_value) and (next_total_cost < energy_budget):
                            neighbour_node.parent_node = current_node.node_name
                            neighbour_node.g_value = next_g_value
                            neighbour_node.total_cost = next_total_cost
                            priority_queue.put((f_cost,dummy_count,neighbour_node))
                            dummy_count += 1
                    else: 
                        # Add to frontier for the first time, only need to check energy constraint
                        if (next_total_cost < energy_budget):
                            neighbour_node.add_to_frontier_before = True
                            neighbour_node.parent_node = current_node.node_name
                            neighbour_node.g_value = next_g_value
                            neighbour_node.total_cost = next_total_cost
                            priority_queue.put((f_cost,dummy_count,neighbour_node))
                            dummy_count += 1

        # Backtracking to find Path
        print(f"Target Reached: {target_reached}")
        print("Returning Path Now...")
        path_data = []
        if target_reached:    
            
            node = node_data[target]
            
            while (node.node_name != source):
                # Call the parent of each Node constantly until it reaches source node, an abitrary decided value to determine the starting node
                path_data.append(node.node_name) # add to path list
                node = node_data[node.parent_node]
            path_data.append(node.node_name)
        return path_data[::-1]

def get_total_distance_and_cost(path_list, dist_dict, cost_dict):
    list_length = len(path_list)
    if (list_length == 1): # Account if source node == target node:
        return (0,0)
    else :
        total_distance = 0
        total_cost = 0
        for i in range(list_length-1):
            current_node = path_list[i]
            next_node = path_list[i+1]
            total_distance += dist_dict[f"{current_node},{next_node}"]
            total_cost += cost_dict[f"{current_node},{next_node}"]
        return (total_distance,total_cost)

def main():
    # Open files
    graph_file = open('G.json','r')
    distance_file = open('Dist.json','r')
    coordinates_file = open('Coord.json','r')
    cost_file = open('Cost.json','r')

    graph_dict = json.load(graph_file)
    dist_dict = json.load(distance_file)
    coord_dict = json.load(coordinates_file)
    cost_dict = json.load(cost_file)

    
    # Define constants
    CONSTRAINT_ENERGY_BUDGET = 287932
    SOURCE_NODE = "1"
    TARGET_NODE = "50" #1358"#"50"


    # Running Code
    graph = Graph()
    start_time = time.time()
    result = graph.shortest_path_ASTAR(SOURCE_NODE, TARGET_NODE, graph_dict, coord_dict, cost_dict, dist_dict, CONSTRAINT_ENERGY_BUDGET)
    total_distance, total_cost = get_total_distance_and_cost(result, dist_dict, cost_dict)
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Shortest Path: " + "->".join(result))
    print("Distance: " + str(total_distance))
    print("Total Cost: " + str(total_cost))

    # Close File
    graph_file.close()
    distance_file.close()
    coordinates_file.close()
    cost_file.close() 

if __name__ == "__main__":
    main()

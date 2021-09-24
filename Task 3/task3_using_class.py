import json
import math
from collections import deque
from queue import PriorityQueue
import time
from typing import final

from networkx.classes import graph
start_time = time.time()

"""
Task 3 Problem Description

You will need to develop an A* search algorithm to solve the NYC instance. The key is to 
develop a suitable heuristic function for the A* search algorithm in this setting.

For tasks 2 and 3, the energy budget is set to be 287932. For all the 3 tasks, the starting and ending 
nodes are set to be ‘1’ and ‘50’, respectively. 

Important Information:
A* Algorithm = Path Cost Function g(n) + Heuristic Function h(n)

Make-up of Path Cost Function: UCS
Make-up of Heuristic Function: Straight line distance to target.

Constraint:
Budget Energy Cost <= 287932
Starting Node: "1"
Target Node: "50"
"""

# ALGORITHM DEVELOPMENT

# Set up
graph_data = open('G.json',) 
graph_dict = json.loads(graph_data.read())
dist_data = open('Dist.json',)
dist_dict = json.loads(dist_data.read())
coord_data = open('Coord.json',)
coord_dict = json.loads(coord_data.read())
cost_data = open('Cost.json',)
cost_dict = json.loads(cost_data.read())

# Define constants
NUMBER_OF_NODES = len(graph_dict.keys())
ROOT_NODE_TERMINATOR = -1
CONSTRAINT_ENERGY_BUDGET = 287932
SOURCE_NODE = "1"
TARGET_NODE = "50" #1358"#"50"

# Set up node information (pre-calculate the h-cost already)
node_dict = {}
for key in graph_dict.keys():
    key_coord = coord_dict[key]
    # distance_to_target = get_straight_line_distance(key_coord, target_coord)
    node_dict[key] = {"node": key, "parent_node": None, "g_value" : -1, "total_cost": -1, "visited":False}
    # node_dict[key] = [False, None, -1, -1, -1] # [Visited, ParentNode, distance_from_source, cost_from_source, distance to target]

class Node():
    def __init__(self, node_name, cooordinates, parent_node, g_value, total_cost, visited):
        self.node_name = node_name
        self.coordinates = cooordinates
        self.parent_node = parent_node
        self.g_value = g_value #cumulative
        self.total_cost = total_cost #cumulative
        self.visited = visited
        
    
class Graph():
    def __init__(self):
        self.node_data = {} 

    def add_node_from_dictionary(self, graph_dictionary, coordinates_dictionary):
        for key in graph_dictionary.keys():
            new_node = Node(node_name=key, cooordinates=coordinates_dictionary[key], parent_node=None, g_value=(-1), total_cost=(-1), visited=False)
            self.node_data[key] = new_node

    def evaluate_heuristic_cost(self, current_coord, target_coord):
        #[x,y] [x1,y1]
        # Heuristic Cost based on distance
        distance = math.dist(current_coord,target_coord)
        return distance

    def get_node_data(self):
        return self.node_data

    

    def shortest_path_ASTAR(self, source, target, node_data, cost_dict, dist_dict):

        source_node = node_data[source]
        target_node = node_data[target]
        dummy_count = 0

        priority_queue = PriorityQueue() # This is a priority queue, using f(n), where f(n) = g(n) + h(n) 
        print("Type of source node" + str(type(source_node)))
        priority_queue.put((0,dummy_count, source_node))
        dummy_count += 1
        

        target_coord =  target_node.coordinates # Get target_coordinates for future multiple calculatations of h(n)

        # Set initial settings for source node
        source_node.parent_node = ROOT_NODE_TERMINATOR
        source_node.g_value = 0
        source_node.total_cost = 0
        
        # Flag to return to tell if shortest path succeeded or not
        target_reached = False
        
        while(priority_queue): # While there is still things in the queue. If not then that means there is no path to the target.

            # Get next node
            _, __, current_node = priority_queue.get()    

            # Exploration Phase
            
            # Check if is target
            if (current_node.node_name == target_node.node_name):
                target_reached  = True
                break # Exit loop as target is found
            elif (current_node.total_cost > CONSTRAINT_ENERGY_BUDGET):
                continue # Do not want to consider this node if energy cost is over budget
            else: 
                # Set visited to true to prevent looping
                current_node.visited = True
                # Adding neighbours to frontier (priority queue)       
                neighbour_nodes = graph_dict[current_node.node_name] # return a list of neighbour nodes

                # We will compute 2 values: g(n) and h(n), where n is the next node
                # g(n) : Distance from source node to this node
                # h(n) : Straight Line Distance from this node to target node (heuristically)
                # f(n) : final evalutative function being f(n) = g(n) + h(n)

                for node in neighbour_nodes:
                    neighbour_node = node_data[node]
                    if neighbour_node.visited != True: # If visited we will not consider anymore. To prevent loopback back to 1
                        neighbour_node.parent_node = current_node.node_name
                        neighbour_node.total_cost = current_node.total_cost + cost_dict[f"{current_node.node_name},{neighbour_node.node_name}"]
                        neighbour_node.g_value = current_node.g_value + dist_dict[f"{current_node.node_name},{neighbour_node.node_name}"]
                        f_cost = neighbour_node.g_value + self.evaluate_heuristic_cost(neighbour_node.coordinates, target_coord)
                        dummy_count += 1
                        priority_queue.put((f_cost,dummy_count,neighbour_node))


        # Preparing stuff to return
        distance_to_target = -1
        energy_cost_to_target = -1
        path_data = []
        

        if target_reached:
            # G-Value == Total Distance from Source
            distance_to_target = target_node.g_value
            # Total_Cost == Total Cost from Source
            energy_cost_to_target = target_node.total_cost
            # Backtracking to find Path
            node = node_data[TARGET_NODE]
            # print("Tyope of node:" + str(type(node)))
            while (node.parent_node != ROOT_NODE_TERMINATOR):
                # Call the parent of each Node constantly until it reaches -1, an abitrary decided value to determine the starting node
                path_data.append(node.node_name) # add to path list
                node = node_data[node.parent_node]
            path_data.append(node.node_name)
        
        return (target_reached, path_data, distance_to_target, energy_cost_to_target)




# Test code
graph = Graph()
graph.add_node_from_dictionary(graph_dict, coord_dict)
result = graph.shortest_path_ASTAR(SOURCE_NODE, TARGET_NODE, graph.get_node_data(), cost_dict, dist_dict)

target_reached = result[0]
path_data = result[1]
distance_from_source_to_target = result[2]
energy_from_source_to_target = result[3]

if (target_reached == False):
    print("Error! Target not found")
else:
    # print(node_dict)
    print("Successul! Target found")
    print("Shortest Path: " + "->".join(path_data[::-1]))
    print("Distance: " + str(distance_from_source_to_target))
    print("Total Cost: " + str(energy_from_source_to_target))
print("--- %s seconds ---" % (time.time() - start_time))
# exit()
# End of test code




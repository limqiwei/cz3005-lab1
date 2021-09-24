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
TARGET_NODE = "50"#"50"

# Set up node information (pre-calculate the h-cost already)
node_dict = {}
for key in graph_dict.keys():
    key_coord = coord_dict[key]
    # distance_to_target = get_straight_line_distance(key_coord, target_coord)
    node_dict[key] = {"node": key, "parent_node": None, "g_value" : -1, "total_cost": -1, "visited":False}
    # node_dict[key] = [False, None, -1, -1, -1] # [Visited, ParentNode, distance_from_source, cost_from_source, distance to target]

# Define functions
def get_straight_line_distance(key_coord, target_coord):
    distance = math.dist(key_coord,target_coord)
    return distance

def returnPath(target_node):
    # Backtracking
    path_array = [] # To fill up given parent node, starting on final node.

    final_node = target_node

    while (node_dict[final_node]["parent_node"] != ROOT_NODE_TERMINATOR):
        # Call the parent of each Node constantly until it reaches -1, an abitrary decided value to determine the starting node
        path_array.append(final_node) # add to path list
        final_node = node_dict[final_node]["parent_node"]
    # At this point the path array contains all the nodes that have been traversed to the end point.
    path_array.append(final_node) # append final node that is the root node
    # print("Path Array Inside Function" + str(path_array))
    path_array.reverse()
    return path_array

def ASTAR(source, target):
    
    # Node tracking
    # Total number of nodes
    # visited_node_array = [False for i in range(NUMBER_OF_NODES)] # Initialize all to False, if visit then will put True
    # parent_node_array = [None for i in range(NUMBER_OF_NODES)] #Set all path to None. This will be used to track the path, can be encapsulated in an 
    priority_queue = PriorityQueue() # This is a priority queue, with 
    priority_queue.put((0, source))
    target_coord = coord_dict[target]
    node_dict[source]["parent_node"] = ROOT_NODE_TERMINATOR
    node_dict[source]["g_value"] = 0
    node_dict[source]["total_cost"] = 0
    
    # print(f"Node 1 : {node_dict[source]}")
    target_reached = False

    while(priority_queue): # While there is still things in the queue. If not then that means there is no path to the target.

        # Get next node
        _ , current_node = priority_queue.get()    

        # Exploration Phase
        
        # Check if is target
        if (current_node == TARGET_NODE):
            target_reached  = True
            break # Exit loop as target is found
        elif (node_dict[current_node]["total_cost"] > CONSTRAINT_ENERGY_BUDGET):
            continue # Do not want to consider this node if energy cost is over budget
        else: 
            # Expand to neighbours
            node_dict[current_node]["visited"] = True
            neighbour_nodes = graph_dict[current_node] # return a list of neighbour nodes

            # At this point to decide which node to add to queue first ()
            # We will compute 2 values: g(n) and h(n), where n is the next node
            # g(n) : Distance from source node to this nnode
            # h(n) : Straight Line Distance from this node to target node (heuristically)

            for node in neighbour_nodes:
                if node_dict[node]["visited"] != True: # If visited we will not consider anymore. To prevent loopback back to 1
                    node_dict[node]["parent_node"] = current_node
                    node_dict[node]["total_cost"] = node_dict[current_node]["total_cost"] + cost_dict[f"{current_node},{node}"] # Compute g_value
                    node_dict[node]["g_value"] = node_dict[current_node]["g_value"] + dist_dict[f"{current_node},{node}"] # Compute g_value
                    f_cost = node_dict[node]["g_value"] + get_straight_line_distance(coord_dict[node], target_coord)
                    priority_queue.put((f_cost,node))

            # # Perform merge sort here (highest priority appended first. Lower f_value => higher priority)
            # sort_by_key(inner_priority_sort_list, "f_value")
            # for node in inner_priority_sort_list:
            #     priority_queue.append(node)
            # Re-loop
    return target_reached

def sort_by_key(list, key_value):
    # print(list)
    list.sort(key=lambda x:node_dict[x]["f_value"])
        

# Test code
result = ASTAR(SOURCE_NODE, TARGET_NODE)
if (result == False):
    print("Error! Target not found")
else:
    # print(node_dict)
    print("Successul! Target found")
    path = returnPath(TARGET_NODE)
    print("Shortest Path: " + "->".join(path))
    print("Distance: " + str(node_dict[TARGET_NODE]["g_value"]))
    
print("--- %s seconds ---" % (time.time() - start_time))
# exit()
# End of test code




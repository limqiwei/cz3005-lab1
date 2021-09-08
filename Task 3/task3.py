import json
from math import sqrt, pow

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




# We define a function that will help us calculate the straight line distance using the coordinates of the current node and the target node.

# Coordinates of Node "1": [-73530767, 41085396]
# Coordinates of Node "50": [-73643471, 41026897]

def getStraightLineDistance(x1,y1,x2,y2):
    x1x2 = x2 - x1
    y1y2 = y2 - y1
    distance = sqrt(pow(x1x2,2)+pow(y1y2,2))
    return distance


node1_node50 = getStraightLineDistance(-73530767,41085396,-73643471,41026897) 
# 112704, 58499
print(node1_node50)







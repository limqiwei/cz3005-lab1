import json
from queue import PriorityQueue

with open ('Dist.json','r') as dist_dictionary:
    distData = json.load(dist_dictionary)

with open ('G.json','r') as graph_dictionary:
    graphData = json.load(graph_dictionary)

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        
    def dijkstra(self, source_vertex, target_vertex):
        visited = set()
        distance = {source_vertex: 0}
        parent_vertex = {source_vertex: None}
        

        pq = PriorityQueue()
        pq.put((0, source_vertex))

        while not pq.empty():
            (_, current_vertex) = pq.get()
            if current_vertex not in visited:
                visited.add(current_vertex)
                
            if current_vertex == target_vertex:
                break

            for neighbor in graphData.get(str(current_vertex)):
                if neighbor not in visited:
                    old_cost = distance.get(neighbor, float('inf'))
                    new_cost = distance[current_vertex] + distData[str(current_vertex) + "," + str(neighbor)]
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distance[neighbor] = new_cost
                        parent_vertex[neighbor] = current_vertex
        
        print("Shortest distance: " + str(distance[target_vertex]))
        return parent_vertex
    
    def goal_path(self, parent, target_vertex):
        if target_vertex not in parent:
            return None
        v = target_vertex
        path_array = []
        while v is not None: # root has null parent
            path_array.append(v)
            v = parent[v]
        return path_array[::-1]


g = Graph(264346)

parent = g.dijkstra('1','50')
path = g.goal_path(parent,'50')
print("Shortest Path: " + " -> ".join(path))
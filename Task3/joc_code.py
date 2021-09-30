import json
from queue import PriorityQueue

with open ('Dist.json','r') as dist_dictionary:
    distData = json.load(dist_dictionary)

with open ('G.json','r') as graph_dictionary:
    graphData = json.load(graph_dictionary)
    
with open ('Cost.json','r') as cost_dictionary:
    costData = json.load(cost_dictionary)

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        
    def dijkstra(self, source_vertex, target_vertex):
        visited = set()
        distance = {source_vertex: 0}
        parent_vertex = {source_vertex: None}
        energy_cost = {source_vertex: 0}

        pq = PriorityQueue()
        pq.put((0, source_vertex))

        while not pq.empty():
            (_, current_vertex) = pq.get()
            #print("current vertex: " + current_vertex)
            #print("parent vertex" + str(parent_vertex))
            if current_vertex not in visited:
                visited.add(current_vertex)
            # print("visited list: " + str(visited))
            if current_vertex == target_vertex:
                break
            #print(graphData.get(str(current_vertex)))
            for neighbor in graphData.get(str(current_vertex)):
                #print("neighbor:"+ str(neighbor))
                if neighbor not in visited:
                    #print(str(neighbor) + "," + str(distance))
                    old_cost = distance.get(neighbor, float('inf'))
                    print(f"Old Cost: {old_cost}, Equality: {old_cost==float('inf')}")
                    # old_cost = float('inf')
                    #print("old cost:"+ str(old_cost))
                    new_cost = distance[current_vertex] + distData[str(current_vertex) + "," + str(neighbor)]
                    #print("new cost:"+ str(new_cost))
                    # old_energy_cost = energy_cost.get(neighbor, float('inf'))
                    #print("old energy cost: " + str(old_energy_cost))
                    new_energy_cost = energy_cost[current_vertex] + costData[str(current_vertex) + "," + str(neighbor)]
                    # print("new energy cost: " + str(new_energy_cost))
                    if new_cost < old_cost and new_energy_cost <= 287932: 
                        pq.put((new_cost, neighbor))
                        #energy_cost = energy_cost + costData[str(current_vertex) + "," + str(neighbor)]
                        #print(energy_cost)
                        distance[neighbor] = new_cost
                        energy_cost[neighbor] = new_energy_cost
                        parent_vertex[neighbor] = current_vertex
                        
        print("Shortest distance: " + str(distance[target_vertex]))
        print("Energy cost: " + str(energy_cost[target_vertex]))
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
#print(parent)
path = g.goal_path(parent,'50')
print("Shortest Path: " + "->".join(path))
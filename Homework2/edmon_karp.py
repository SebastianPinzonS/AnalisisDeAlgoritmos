import time 
import sys
from collections import deque

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.flow_matrix = [[0] * size for _ in range(size)]
        self.size = size
    
    def add_edge(self, source, destination, capacity):
        if self.adj_matrix[source][destination] > 0:
            return
        self.adj_matrix[source][destination] = capacity
        
    def bfs(self, source, destination, parent):
        visited = [False] * self.size
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.adj_matrix[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == destination:
                        return True
        return False
    
    def edmond_karp(self, source, destination):
        start_time = time.time()
        parent = [-1] * self.size
        max_flow = 0
        
        while self.bfs(source, destination, parent):
            path_flow = float('inf')
            v = destination
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.adj_matrix[u][v])
                v = parent[v]
            v = destination
            while v != source:
                u = parent[v]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow
                self.flow_matrix[u][v] += path_flow
                self.flow_matrix[v][u] -= path_flow
                v = parent[v]
            
            max_flow += path_flow
            
        execution_time = time.time() - start_time
        return max_flow, execution_time
    
    def print_flow(self, filename='edmon_karp_output.txt', max_flow=0, execution_time=0):
        with open(filename, 'w') as file:
            file.write("Edmond Karp Algorithm\n")
            file.write("Max flow per edge:\n")
            for i in range(self.size):
                for j in range(self.size):
                    if self.flow_matrix[i][j] > 0:
                        file.write(f"{i} -> {j}: {self.flow_matrix[i][j]}\n")
            file.write(f"Max flow: {max_flow}\n")
            file.write(f"Execution time: {execution_time} seconds\n")

def create_graph_from_file(filepath):
    with open(filepath, 'r') as file:
        num_vertex = int(file.readline())
        graph = Graph(num_vertex)
        for line in file.readlines():
            source, destination, capacity = map(int, line.split(","))
            graph.add_edge(source, destination, capacity)
    return graph

if __name__ == '__main__':
    if len(sys.argv) != 2:
       print("Incorrect usage, instead try: python min_cost_double_way.py <txt_file>")
       sys.exit(1)  
    filepath = sys.argv[1]
    
    graph = create_graph_from_file(filepath)
    max_flow, execution_time = graph.edmond_karp(0, graph.size - 1)
    graph.print_flow(max_flow=max_flow, execution_time=execution_time)  # Print the flow matrix
    
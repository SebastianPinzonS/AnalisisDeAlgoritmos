import sys
import copy
import time
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

    def print_flow(self, file, max_flow=0, execution_time=0):
        file.write("Edmond Karp Algorithm\n")
        file.write("Max flow per edge:\n")
        for i in range(self.size):
            for j in range(self.size):
                if self.flow_matrix[i][j] > 0:
                    file.write(f"{i} -> {j}: {self.flow_matrix[i][j]}\n")
        file.write(f"Max flow: {max_flow}\n")
        file.write(f"Execution time: {execution_time} seconds\n")

# Push-Relabel implementation
def flowOperation(graph:dict, u:int, v:int, d:int):
    if d <= graph[u][v]:
        graph[u][v] = graph[u][v] - d 
        graph[v][u] = graph[v][u] + d

def pointerOperation(pointerArray:list, v:int):
    v = pointerArray.pop(v)
    pointerArray.insert(0,v)

def changeHeight(helper:list,v:int,n:int):
    helper[v][1] = n

def getHeight(helper:list,v:int):
    return helper[v][1]

def changeExcess(helper:list,v:int,n:int):
    if v != 0:
        helper[v][0] = helper[v][0] + n

def getExcess(helper:list,v:int):
    return helper[v][0]

def getMaxFlow(graph:dict):
    flow = sum(graph[n][0] for n in graph[0])
    return flow

def initPR(graph:dict, nv:int):
    pointerArray = [k for k in graph.keys()]
    pointerArray.pop(0)
    pointerArray.pop(-1)
    helper = {i:[0,0] for i in graph}
    helper[0][0], helper[0][1] = None, nv

    for i in range(1,len(graph)-1):
        helper[i][0], helper[i][1] = 0, 0 

    helper[nv-1][0], helper[nv-1][1] = 0,0

    for v in graph[0]:
        changeExcess(helper, v, graph[0][v])
        flowOperation(graph,0,v,graph[0][v])

    return helper, pointerArray

def push(helper,graph:dict,u:int,v:int):
    d = min(getExcess(helper,u),graph[u][v])
    flowOperation(graph,u,v,d)
    changeExcess(helper,u,-d)
    changeExcess(helper,v,+d)   

def pushRelabel(graph, nv):
    start_time = time.time()
    helper, pointerArray = initPR(graph,nv) 
    p = 0
    while p < len(pointerArray):
        u = pointerArray[p]
        if getExcess(helper,u) > 0:
            for v in graph[u]:
                if getHeight(helper,v) +1 == getHeight(helper,u):
                    push(helper,graph,u,v)
            if getExcess(helper,u) > 0:
                newH = min(getHeight(helper,v) for v in graph[u] if graph[u][v] > 0 ) + 1 
                changeHeight(helper,u,newH)
                pointerOperation(pointerArray,p)
                p = 0
            else:
                p += 1
        else:
            p += 1
    execution_time = time.time() - start_time
    return execution_time

def getEdgeFlows(residual_graph, original_capacity):
    flow_values = {}
    for u in original_capacity:
        flow_values[u] = {}
        for v in original_capacity[u]:
            residual_cap = residual_graph.get(u, {}).get(v, 0)
            original_cap = original_capacity[u][v]
            flow_values[u][v] = original_cap - residual_cap
    return flow_values

def print_push_relabel_results(flow_values, max_flow, execution_time, file):
    file.write("\nPush-Relabel Algorithm\n")
    file.write("Max flow per edge:\n")
    for u in flow_values:
        for v in flow_values[u]:
            if flow_values[u][v] > 0:
                file.write(f"{u} -> {v}: {flow_values[u][v]}\n")
    file.write(f"Max flow: {max_flow}\n")
    file.write(f"Execution time: {execution_time} seconds\n")

def load_graph_from_csv(filepath):
    # For Push-Relabel
    graph_dict = {}
    # For Edmonds-Karp
    with open(filepath, 'r') as f:
        nv = int(f.readline().strip())
        graph_ek = Graph(nv)
        
        for line in f:
            u, v, cap = map(int, line.strip().split(','))
            
            # For Push-Relabel
            if u not in graph_dict:
                graph_dict[u] = {}
            if v not in graph_dict:
                graph_dict[v] = {}
            graph_dict[u][v] = cap
            graph_dict[v][u] = 0
            
            # For Edmonds-Karp
            graph_ek.add_edge(u, v, cap)
    
    graph_dict = dict(sorted(graph_dict.items()))
    return graph_dict, graph_ek, nv

def main():
    if len(sys.argv) != 2:
        print("Usage: python flow_algorithms.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    output_file = "flow_algorithms_output.txt"
    
    # Load graphs for both algorithms
    graph_dict, graph_ek, nv = load_graph_from_csv(filepath)
    
    with open(output_file, 'w') as file:
        # Run and output Edmonds-Karp first
        ek_max_flow, ek_execution_time = graph_ek.edmond_karp(0, nv - 1)
        graph_ek.print_flow(file, max_flow=ek_max_flow, execution_time=ek_execution_time)
        
        # Run and output Push-Relabel second
        original_graph = copy.deepcopy(graph_dict)
        pr_execution_time = pushRelabel(graph_dict, nv)
        pr_max_flow = getMaxFlow(graph_dict)
        flow_values = getEdgeFlows(graph_dict, original_graph)
        print_push_relabel_results(flow_values, pr_max_flow, pr_execution_time, file)
    
    # Print to console for verification
    print(f"\nResults have been written to '{output_file}'")
    print(f"Push-Relabel max flow: {pr_max_flow}")
    print(f"Edmonds-Karp max flow: {ek_max_flow}")

if __name__ == "__main__":
    main()

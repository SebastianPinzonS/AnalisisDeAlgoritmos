import sys

def has_cycle(graph):
    
    visited = {}
    stack = {}
    for v in graph:
        visited[v]=False
        stack[v]=False
    for v in graph:
        if visited[v] == False and detect_cycle(graph,v,visited,stack):
            return True
    return False


def detect_cycle(graph,v,visited,stack):
    if visited[v] == False:
        visited[v]=True
        stack[v]=True
        for v1 in graph[v]:
            if v1 != '':
                if visited[v1] == False and detect_cycle(graph,v1,visited,stack):
                    return True
                elif stack[v1]:
                    return True
    stack[v]=False
    return False


def process_csv_to_graph(filepath):
    graph = {}
    with open(filepath, 'r') as file:
       next(file)  # Skip first line
       for line in file:
           row = line.strip().split(',')
           values = row[1:]
           graph[row[0]]=values
    return graph

if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("Incorrect usage, instead try: python lending_chain.py <csv_file>")
       sys.exit(1)  
    filepath = sys.argv[1]
    graph = process_csv_to_graph(filepath)
    print(has_cycle(graph))
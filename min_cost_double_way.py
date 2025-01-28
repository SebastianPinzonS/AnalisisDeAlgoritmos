import sys


def prim_algorithm(edges, num_nodes):
    """
    Function to implement Prim's algorithm to find the minimum spanning tree
    of a graph.
    :param edges: List of edges in the graph. Each edge is represented as (u, v, weight)
    :param num_nodes: Number of nodes in the graph
    :return: List of edges in the minimum spanning tree
    """
    graph = {i: {} for i in range(num_nodes)}
    for u, v, weight in edges:
        # Since it's an undirected graph, add the edge in both directions
        graph[u][v] = weight
        graph[v][u] = weight

    visited = []
    edges_to_consider = []
    mst_edges = []

    # Start from the first node
    start_node = 0
    visited.append(start_node)
    for neighbor, weight in graph[start_node].items():
        edges_to_consider.append((start_node, neighbor, weight))

    while edges_to_consider and len(visited) < num_nodes:
        # Sort edges to consider by weight, taking the one with the smallest weight
        edges_to_consider.sort(key=lambda x: x[2])
        u, v, weight = edges_to_consider.pop(0)
        
        # If the target node has already been visited, skip it to avoid cycles
        if v in visited:
            continue

        # Add the edge with the smallest weight to the MST
        mst_edges.append((u, v, weight))

        # Add the target node to the visited list to avoid cycles
        visited.append(v)

        # Consider all edges connected to the newly added node
        for neighbor, weight in graph[v].items():
            if neighbor not in visited:
                edges_to_consider.append((v, neighbor, weight))

    # Check if all nodes were visited; if not, the graph is not connected
    if len(visited) < num_nodes:
        raise Exception('The graph is not connected')

    return mst_edges

def process_txt_file(filepath):
    with open(filepath, 'r') as file:
        num_node = int(file.readline())
        edges = []

        for line in file.readlines():
            edge = tuple(map(int, line.split(" ")))
            edges.append(edge)
    return num_node, edges

if __name__ == '__main__':
    if len(sys.argv) != 2:
       print("Incorrect usage, instead try: python min_cost_double_way.py <txt_file>")
       sys.exit(1)  
    filepath = sys.argv[1]

    num_nodes, edges = process_txt_file(filepath)
    
    mst = prim_algorithm(edges, num_nodes)

    print("Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"Edge ({u}, {v}) - Weight: {weight}")

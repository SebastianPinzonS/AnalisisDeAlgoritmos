import sys,copy,time

def flowOperation(graph:dict, u:int, v:int, d:int): #Funcion que altera el grafo y el grafo recidual
    if d <= graph[u][v]:
        graph[u][v]= graph[u][v] -d 
        graph[v][u]= graph[v][u] +d

def pointerOperation(pointerArray:list, v:int): # Funcion que pone en el primer lugar del array el vertice
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
    pointerArray = [k for k in graph.keys()] # Estructura usada como simulacion de un array con apuntador para hacer seleccion de push
    pointerArray.pop(0)
    pointerArray.pop(-1)
    helper = {i:[0,0] for i in graph} # Estructura que contiene los excesos y alturas de los vertices
    helper[0][0], helper[0][1] = None, nv

    for i in range(1,len(graph)-1):
        helper[i][0], helper[i][1] = 0, 0 

    helper[nv-1][0], helper[nv-1][1] = 0,0

    for v in graph[0]: # Este ciclo hace el push desde el origen hacia los vertices vecinos iniciando el preflujo
        changeExcess(helper, v, graph[0][v])
        flowOperation(graph,0,v,graph[0][v])

    return helper, pointerArray

def push(helper,graph:dict,u:int,v:int):
    d = min(getExcess(helper,u),graph[u][v])
    flowOperation(graph,u,v,d)
    changeExcess(helper,u,-d)
    changeExcess(helper,v,+d)   

def load_graph_from_csv(filepath):
    graph = {}
    vertices = set()
    
    with open(filepath, 'r') as f:
        nv = int(f.readline().strip())
        
        for line in f:
            u, v, cap = map(int, line.strip().split(','))
            
            vertices.add(u)
            vertices.add(v)
            
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
                
            graph[u][v] = cap  
            graph[v][u] = 0    
    
    graph = dict(sorted(graph.items()))
    
    if len(vertices) != nv:
        print(f"Warning: Expected {nv} vertices but found {len(vertices)}")
    
    return graph, nv
     

def pushRelabel(graph, nv):
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

def getEdgeFlows(residual_graph, original_capacity):

    flow_values = {}

    for u in original_capacity:
        flow_values[u] = {}
        for v in original_capacity[u]:
            residual_cap = residual_graph.get(u, {}).get(v, 0)
            original_cap = original_capacity[u][v]
            
            flow_values[u][v] = original_cap - residual_cap
            
    
    return flow_values

def printEdgeFlows(flow_values):
   
    for u in flow_values:
        for v in flow_values[u]:
            if flow_values[u][v] > 0:  
                print(f"Eje {u}->{v}: Flujo = {flow_values[u][v]}")

def main():
    filepath = sys.argv[1]
    graph,nv = load_graph_from_csv(filepath)
    originalGraph = copy.deepcopy(graph)
    start = time.time()
    pushRelabel(graph,nv)
    maxFlow = getMaxFlow(graph)
    print("El flujo maximo es: " + str(maxFlow))
    printEdgeFlows(getEdgeFlows(graph,originalGraph))
    end = time.time()
    print(f"La funcion demoro: {end - start:.4f} seconds" )



    
if __name__ == "__main__":
    main()

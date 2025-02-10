import sys

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

def initPR(graph:dict):
    pointerArray = [k for k in graph.keys()] # Estructura usada como simulacion de un array con apuntador para hacer seleccion de push
    pointerArray.pop(0)
    pointerArray.pop(-1)
    helper = {i:[0,0] for i in graph} # Estructura que contiene los excesos y alturas de los vertices
    helper[0][0], helper[0][1] = None, len(graph)

    for i in range(1,len(graph)-1):
        helper[i][0], helper[i][1] = 0, 0 

    helper[len(graph)-1][0], helper[len(graph)-1][1] = 0,0

    for v in graph[0]: # Este ciclo hace el push desde el origen hacia los vertices vecinos iniciando el preflujo
        changeExcess(helper, v, graph[0][v])
        flowOperation(graph,0,v,graph[0][v])

    return helper, pointerArray

def push(helper,graph:dict,u:int,v:int):
    d = min(getExcess(helper,u),graph[u][v])
    flowOperation(graph,u,v,d)
    changeExcess(helper,u,-d)
    changeExcess(helper,v,+d)   

def relabel(graph,i):
    pass

def load_graph_from_csv(filepath):
    graph = {}
    vertices = set()

    with open(filepath, 'r') as f:
        next(f)
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
    return graph
     

def pushRelabel(graph):
    helper, pointerArray = initPR(graph) 
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
    return(getExcess(helper,-1))

def main():
    filepath = sys.argv[1]
    graph = load_graph_from_csv(filepath)
    maxFlow = pushRelabel(graph)
    print("El flujo maximo es: " + maxFlow)
    
if __name__ == "__main__":
    main()
import sys

def has_cycle(graph):
    """
    Detecta si hay un ciclo en un grafo dirigido usando DFS (búsqueda en profundidad).
    Retorna True si encuentra un ciclo, False en caso contrario.
    """
    # Diccionarios para rastrear nodos visitados y la pila de recursión
    visited = {v: False for v in graph}
    stack = {v: False for v in graph}
    
    # Revisa cada nodo del grafo
    for v in graph:
        if not visited[v] and detect_cycle(graph, v, visited, stack):
            return True
    return False

def detect_cycle(graph, v, visited, stack):
    """
    Función auxiliar para detectar ciclos usando DFS.
    v: nodo actual que estamos visitando
    """
    visited[v] = True  # Marca el nodo como visitado
    stack[v] = True    # Añade el nodo a la pila de recursión
    
    # Revisa cada vecino del nodo actual
    for neighbor in graph[v]:
        if not visited[neighbor] and detect_cycle(graph, neighbor, visited, stack):
                return True
        elif stack.get(neighbor, False):  # Si el vecino está en la pila, hay un ciclo
            return True
    
    stack[v] = False  # Retira el nodo de la pila al terminar
    return False

def process_csv_to_graph(filepath):
    """
    Procesa un archivo CSV y lo convierte en un grafo.
    Retorna un diccionario que representa la lista de adyacencia.
    """
    try:
        graph = {}
        with open(filepath, 'r') as file:
            next(file)  # Salta la línea de encabezado
            for line in file:
                row = line.strip().split(',')
                if row:  # Verifica que la fila no esté vacía
                    node = row[0]
                    # Filtra vecinos vacíos
                    neighbors = [n for n in row[1:] if n.strip()]
                    graph[node] = neighbors
        return graph
    except FileNotFoundError:
        print(f"Error: Archivo '{filepath}' no encontrado")
        sys.exit(1)
    except Exception as e:
        print(f"Error procesando el archivo: {str(e)}")
        sys.exit(1)

def main():
    # Verifica que se proporcione el archivo CSV como argumento
    if len(sys.argv) != 2:
        print("Uso: python lending_chain.py <archivo_csv>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    graph = process_csv_to_graph(filepath)
    
    # Verifica que el grafo no esté vacío
    if not graph:
        print("Error: El grafo está vacío")
        sys.exit(1)
    
    # Ejecuta la detección de ciclos y muestra el resultado
    has_cycle_result = has_cycle(graph)
    if has_cycle_result:
        print("Se ha detectado un auto prestamo")
    else:
        print("NO se ha detectado un auto prestamo") 

if __name__ == "__main__":
    main()

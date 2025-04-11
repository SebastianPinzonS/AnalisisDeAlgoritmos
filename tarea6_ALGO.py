import random
import sys
import time


### FUNCIONES PRIMER ALGORITMO APROXIMADO CUBRIMIENTO DE VERTICES ###
def vertex_cover_approx_first_version(edges):
    cover = set()
    while edges:
        edge = random.choice(edges)
        u, v = edge
        edges.remove(edge)
        cover.add(u)
        cover.add(v)
        edges = [(x, y) for (x, y) in edges if x not in (u, v) and y not in (u, v)]
    return cover


### FUNCIONES SEGUNDO ALGORITMO APROXIMADO CUBRIMIENTO DE VERTICES ###

def vertex_cover_approx_second_version(edges):
    cover = set()
    while edges:
        grade_vertex = get_vertex_grades(edges)
        max_grade_vertex = max(grade_vertex, key=lambda x: len(grade_vertex[x]))
        cover.add(max_grade_vertex)
        edges = [(u, v) for (u, v) in edges if max_grade_vertex not in (u, v)]
    return cover


### FUNCIONES TERCER ALGORITMO APROXIMADO CUBRIMIENTO DE VERTICES ###
def vertex_cover_approx_third_version(edges):
    cover = set()
    while edges:
        max_local_grade = None
        edge = random.choice(edges)
        u, v = edge
        grades_vertex = get_vertex_grades(edges)
        if len(grades_vertex[u]) >=len(grades_vertex[v]):
            max_local_grade = u
        else:
            max_local_grade = v
        cover.add(max_local_grade)
        edges = [(u, v) for (u, v) in edges if max_local_grade not in (u, v)]
    return cover

### FUNCIONES CUARTO ALGORITMO APROXIMAOD CUBRIMIENTO DE VERTICES ###
def vertex_cover_approx_fourth_version(edges):
    cover = set()
    while edges:
        edge = random.choice(edges)
        u, v = edge
        chosen = random.choice([u,v])
        cover.add(chosen)
        edges = [(u, v) for (u, v) in edges if chosen not in (u, v)]
    return cover

### FUNCIONES GENERALES ###

def get_vertex_grades(edges):
    vertex_grade = {}
    for (u,v) in edges:
        vertex_grade.setdefault(u,[]).append(v)
        vertex_grade.setdefault(v,[]).append(u)
    return vertex_grade

def parse_graph(graph_str):
    edges = []
    for line in graph_str.splitlines():
        if line.strip():
            parts = line.split('\t')
            if len(parts) == 2:
                u, v = map(int, parts)
                edges.append((u, v))
    return edges


if __name__ == '__main__':

    algorithms = {
        1: vertex_cover_approx_first_version,
        2: vertex_cover_approx_second_version,
        3: vertex_cover_approx_third_version,
        4: vertex_cover_approx_fourth_version,
    }


    filename = sys.argv[1]
    try:
        number_algorithms = int(sys.argv[2])
    except Exception as ex:
        print(ex)

    try:
        with open(filename,'r') as file:
            content = file.read()
    except Exception as ex:
        print("Problema al intentar leer el archivo de grafos",ex)
        sys.exit(1)

    edges = parse_graph(content)

    approximate_algorithm = algorithms[number_algorithms]

    start_time = time.time()
    cover_set = approximate_algorithm(edges)
    end_time = time.time()

    execution_time = end_time - start_time


    print("Vértices del cubrimiento:", cover_set)
    print("Tamaño del conjunto de vértices:", len(cover_set))
    print("Tiempo de ejecución: {:.6f} segundos.".format(execution_time))



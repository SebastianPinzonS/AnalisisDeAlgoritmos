
# Análisis de Flujos Máximos: Edmonds-Karp y Push-Relabel

Esta aplicación implementa dos algoritmos para resolver el problema de flujo máximo en una red:

- **Edmonds-Karp**: Utiliza búsquedas en anchura (BFS) para encontrar caminos aumentantes.
- **Push-Relabel**: Mejora la asignación de flujo mediante el uso de "pre-fujos" y relabeling.

Se usa un único archivo de entrada para definir la red (o grafo) y ambos algoritmos se ejecutan en el mismo script, generando un archivo de salida con los resultados.

---

## 1. Formato del Archivo de Entrada

El archivo de entrada debe ser un archivo de texto (por ejemplo, CSV) con el siguiente formato:

- **Primera línea**: Un entero que indica el número de nodos (`nv`) presentes en el grafo.
- **Líneas subsiguientes**: Cada línea representa una arista de la red con el siguiente formato (valores separados por comas):

  ```
  u,v,capacidad
  ```

  donde:
  - `u` : Nodo de origen (entero).
  - `v` : Nodo de destino (entero).
  - `capacidad` : Capacidad de la arista (entero).

**Ejemplo de archivo (flow_network.csv):**

```
5
0,1,16
0,2,13
1,2,10
1,3,12
2,1,4
2,4,14
3,2,9
3,5,20
4,3,7
4,5,4
```

---

## 2. Ejecución del Script

Para ejecutar el script, sigue estos pasos:

1. Asegúrate de tener instalado Python 3.
2. Guarda el código en un archivo llamado, por ejemplo, `flow_algorithms.py`.
3. Ejecuta el script desde la terminal pasando el archivo de entrada como argumento:

   ```bash
   python main.py <ruta_al_archivo_de_entrada>
   ```

**Ejemplo de ejecución:**

```bash
python main.py flow_network.csv
```

El script generará un archivo de salida llamado `flow_algorithms_output.txt`, donde se registrarán los resultados de ambos algoritmos.

---

## 3. Salida del Programa

El archivo de salida (`flow_algorithms_output.txt`) contendrá lo siguiente:

### Sección "Edmond Karp Algorithm"

- **Listado de cada arista con flujo asignado** (se muestran aquellas con flujo > 0).
- **Flujo máximo alcanzado** desde el nodo fuente (nodo 0) hasta el sumidero (último nodo, `nv - 1`).
- **Tiempo de ejecución** del algoritmo.

**Ejemplo de salida (parcial):**

```
Edmond Karp Algorithm
Max flow per edge:
0 -> 1: 12
1 -> 3: 12
...
Max flow: 23
Execution time: 0.0023 seconds
```

### Sección "Push-Relabel Algorithm"

- **Listado del flujo asignado a cada arista** (se muestran sólo aquellas con flujo positivo).
- **Flujo máximo calculado** mediante el método preflujo-push-relabel.
- **Tiempo de ejecución** del algoritmo.

**Ejemplo de salida (parcial):**

```
Push-Relabel Algorithm
Max flow per edge:
0 -> 2: 13
2 -> 4: 13
...
Max flow: 23
Execution time: 0.0019 seconds
```

Además, los resultados se imprimirán en la consola para facilitar la verificación, mostrando el flujo máximo obtenido por cada uno de los dos métodos.


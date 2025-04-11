# Taller de Cubrimiento de Vértices: Algoritmos Aproximados

---

## **Enunciado del Problema**

Implementar, en el marco de los grupos de trabajo, un programa que resuelva el problema de cubrimiento de vértices utilizando los siguientes 4 algoritmos aproximados:

1. **Algoritmo 1:**  
   Escoger arbitrariamente un eje, incluir los dos vértices conectados, descartar todos los demás ejes conectados por los vértices escogidos y repetir hasta que no queden ejes.
2. **Algoritmo 2:**  
   Escoger el vértice de mayor grado, descartar los ejes que llegan al vértice escogido y repetir hasta que no queden ejes.
3. **Algoritmo 3:**  
   Escoger arbitrariamente un eje, incluir el vértice de mayor grado de los dos vértices conectados por el eje, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.
4. **Algoritmo 4:**  
   Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos vértices conectados, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.

El programa debe recibir como entrada:

- **Un archivo de texto:**  
  Cada línea contiene una pareja de números (enteros) que representan dos vértices conectados, separados por tab.
  
- **Un número (1, 2, 3 o 4):**  
  Indica el algoritmo aproximado a ejecutar.

El programa deberá imprimir en pantalla:

- Los vértices que conforman el cubrimiento.
- El tamaño del conjunto de vértices encontrado.

---

## **Formato del Archivo de Entrada**

El archivo de entrada debe ser un archivo de texto plano (`.txt`) con el siguiente formato:

- **Cada línea** representa un eje del grafo.
- **Cada línea** contiene dos números separados por tab.

#### Ejemplo de Archivo (`graph.txt`):
```
    1	5
    1	4
    2	3
    2	6
    3	4
    4	5
    4	6
    5	7
```

## **Ejecutar el Programa**

### **Requisitos:**

- Tener **Python 3** instalado en el sistema.

### **Instrucciones de Uso:**

1. Descarga y descomprime el archivo `tarea6_ALGO.zip`, el cual contiene:
   - El código fuente (`tarea6_ALGO.py`).
   - Este README.
   - Un archivo Excel (`Resultados ejecuciones grafos.xlsx`) con los resultados de las ejecuciones de los grafos de 100, 1000 y 10000 con los 4 algoritmos, donde se detalla el tiempo de ejecución y la longitud de los vértices de cubrimiento mínimo.

2. Para ejecutar el programa, se abre una terminal o consola y se usa el siguiente comando:

   ```bash
   python tarea6_ALGO.py <grafo_edges_<numero de vertices (100,1000,10000)>.txt> <numero_algoritmo>


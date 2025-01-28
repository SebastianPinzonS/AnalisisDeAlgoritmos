
# Análisis de Grafos: Calles de Doble Vía y Detección de Autopréstamos


---

## 🛣️ Conversión de Calles a Doble Vía con Costo Mínimo

### **Enunciado**
Una ciudad se diseño de tal modo que todas sus calles fueran de una sola vía. Con el paso del
tiempo la cantidad de habitantes de la ciudad creció y esto produjo grandes trancones en algunas de
las vias debido a algunos desvíos innecesarios que tienen que tomar los habitantes de la ciudad para
poder llegar a sus trabajos. Por lo tanto, el alcalde tomó la decisión de ampliar algunas vias para que
puedan convertirse en doble via. Dado el mapa de la ciudad y el costo de convertir cada via actual en
doble via, determinar qué vias se deben convertir, de modo que se pueda transitar de cualquier punto
a cualquier punto de la ciudad por dobles vias y que el costo de la conversión sea el mínimo posible.

---

### 📜 Formato del Archivo de Entrada

El archivo debe ser de texto plano con el siguiente formato:

1. **Primera línea**: Número de nodos en el grafo (entero).
2. **Líneas siguientes**: Cada línea representa una arista del grafo con el formato:
   ```
   u v peso
   ```
   Donde:
   - `u`: Nodo de inicio (entero).
   - `v`: Nodo de destino (entero).
   - `peso`: Costo de convertir la arista en doble vía (entero).

#### Ejemplo de Archivo (`city_graph.txt`):
```
5
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9
```

---

### ▶️ Cómo Ejecutar el Script

1. Asegúrate de tener **Python 3** instalado.
2. Guarda el script como `min_cost_double_way.py`.
3. Ejecuta el script desde la terminal con el comando:
   ```bash
   python min_cost_double_way.py <archivo_entrada>
   ```
   Reemplaza `<archivo_entrada>` con la ruta al archivo.

#### Ejemplo:
```bash
python min_cost_double_way.py city_graph.txt
```

---

### 📊 Salida del Programa

El programa imprimirá el **Árbol de Expansión Mínima (MST)** con las aristas seleccionadas y sus pesos.

#### Ejemplo de Salida:
```
Árbol de Expansión Mínima (MST):
Arista (0, 1) - Peso: 2
Arista (1, 2) - Peso: 3
Arista (1, 4) - Peso: 5
Arista (0, 3) - Peso: 6
```

Esto muestra las aristas del MST y los costos asociados.

---

## 🏦 Detección de Autopréstamos en Sistemas Bancarios

### **Enunciado**
 La Superintendencia Bancaria tiene un registro de préstamos que cada entidad bancaria hace a otra
en el país. Con esta información, la Superintendencia está interesada en detectar si hay autopréstamos
en el sistema. Además de casos de prestamos directos de una entidad a si misma, una autoprestamo
también puede ser un esquema en el que una entidad se presta plata a si misma a traves de una
cadena de prestamos que inicia y termina en la misma entidad. Dada la relación p de prestamos entre
entidades, determinar si existe algún autopréstamo.

---

### 📜 Formato del Archivo de Entrada

El archivo debe ser un **CSV** con dos columnas:
- **`bank`**: Nombre de la entidad bancaria.
- **`lending_to`**: Lista de bancos a los que presta dinero, separados por comas.

#### Ejemplo de Archivo (`has_chain.csv`):
```
bank,lending_to
JPMorgan Chase,Wells Fargo,Deutsche Bank,Goldman Sachs,BNP Paribas
Wells Fargo,Morgan Stanley,JPMorgan Chase,Barclays
Morgan Stanley,Deutsche Bank,Goldman Sachs,Société Générale
Deutsche Bank,BNP Paribas,Goldman Sachs,HSBC
Goldman Sachs,JPMorgan Chase,Deutsche Bank,BBVA
BNP Paribas,Deutsche Bank,Santander,Morgan Stanley
Credit Suisse,JPMorgan Chase,UBS,Wells Fargo
HSBC,Deutsche Bank,BNP Paribas,Credit Suisse
Barclays,Credit Suisse,HSBC,Morgan Stanley
Santander,BNP Paribas,UniCredit,Deutsche Bank
Société Générale,
BBVA,
UBS,
UniCredit,
ING,
Standard Chartered,
RBS,
```

#### Archivo sin Ciclos (`no_chain.csv`):
```
bank,lending_to
JPMorgan Chase,Wells Fargo,Deutsche Bank,Goldman Sachs,BNP Paribas
Wells Fargo,Morgan Stanley,Barclays,Credit Suisse
Morgan Stanley,Société Générale,BBVA,HSBC
Deutsche Bank,Credit Suisse,Santander,UBS
Goldman Sachs,UniCredit,BBVA,ING
BNP Paribas,Santander,UniCredit,Standard Chartered
Credit Suisse,UBS,Barclays,ING
HSBC,Standard Chartered,RBS,Santander
Barclays,RBS,Standard Chartered,UniCredit
Santander,BBVA,ING,RBS
Société Générale,
BBVA,
UBS,
UniCredit,
ING,
Standard Chartered,
RBS,
```

---

### ▶️ Cómo Ejecutar el Script

1. Asegúrate de tener **Python 3** instalado.
2. Guarda el script como `lending_chain.py`.
3. Ejecuta el script desde la terminal con el comando:
   ```bash
   python lending_chain.py <archivo_csv>
   ```
   Reemplaza `<archivo_csv>` con la ruta al archivo CSV.

#### Ejemplo:
```bash
python lending_chain.py has_chain.csv
```

---

### 📊 Salida del Programa

El programa devuelve:
- `True` si existe al menos un ciclo (autopréstamo).
- `False` si no hay ciclos en el grafo.

#### Ejemplo de Salida:
**Con archivo `has_chain.csv`:**
```
True
```

**Con archivo `no_chain.csv`:**
```
False
```

---

## ⚠️ Notas Importantes

### Para ambos scripts:
1. **Formato de Entrada**:
   - Asegúrate de que los archivos sigan el formato especificado.
   - Revisa que las columnas, nodos y pesos estén correctamente definidos.

2. **Conectividad del Grafo (MST)**:
   - El grafo debe ser conexo para obtener un Árbol de Expansión Mínima (MST). Si no lo es, el programa mostrará un error:
     ```
     The graph is not connected
     ```

3. **Ciclos en Prestamos**:
   - El programa identifica ciclos en grafos dirigidos. Si no existen conexiones entre los nodos o no hay un ciclo, el resultado será `False`.


# README

Este programa construye un arreglo de sufijos a partir de un archivo de texto y, luego, busca las posiciones en las que aparecen una serie de consultas (cada consulta en una línea de otro archivo).

## Archivos de Entrada

1. Un archivo de texto, por ejemplo "text.txt". Puede tener varias líneas.  
2. Un archivo de consultas, por ejemplo "queries.txt". Cada línea representa una cadena a buscar.

## Uso

Desde la terminal, ejecuta:

   python suffix_array_search.py <archivo_texto> <archivo_consultas> [<archivo_salida>]

   Donde:
   - <archivo_texto> es el nombre del archivo que contiene el texto completo.  
   - <archivo_consultas> es el nombre del archivo con una consulta por línea.  
   - <archivo_salida> (opcional) indica el archivo donde se guardarán los resultados; si no se especifica, se mostrarán en pantalla.

## Ejemplo

Si tenemos un archivo "text.txt" con "Mississippi" y un archivo "queries.txt" con:

  i  
  ssi  
  xyz  

Al ejecutar:

  python suffix_array_search.py text.txt queries.txt resultados.txt

Se construirá el arreglo de sufijos para "Mississippi", y se buscarán las consultas. El programa escribirá los resultados en "resultados.txt", mostrando las posiciones donde aparece cada consulta. Si una consulta no se encuentra, aparece la consulta sin posiciones.

## Notas

- Si una consulta está repetida en el archivo de consultas, se repite la búsqueda exactamente igual.
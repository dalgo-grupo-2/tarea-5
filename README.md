# Integrantes

- Sergio Pardo [@SergioPardo55](https://github.com/SergioPardo55)
- Juan Diego Calixto [@jcalixto202020774](https://github.com/jcalixto202020774)
- Juan Diego Yepes [@juanyepesp](https://github.com/juanyepesp)


# Cómo ejecutar este programa:

Para compilar y ejecutar este programa seguir las siguientes instrucciones:

1. Abrir una consola.

2. Ir a la carpeta fuente donde usted haya clonado este repositorio localmente.

`cd C:\Usuarios\juan\carpeta1\carpeta2\...\`

3. Hacer referencia al archivo del algoritmo que desea ejecutar, por ejemplo

`python dfs.py < distances5.txt`


# Especificaciones:

Parte 1: Para probar los algoritmos de Dijkstra, Bellman Ford y Floyd Warshall puede utilizar cualquier `distances` o `distances_costosminimos`. Además de esto, hay 2 archivos adicionales, `distancesDisconnected.txt` y `distances5ciclo.txt`, para probar casos especiales en estos algoritmos. 

Parte 2: Para probar el BFS se pueden utilizar los archivos de distances, ya sea de los desconectados como `distancesDisconnected.txt` o `distances100.txt`. El retorno es una lista de listas donde cada sublista es una particion del grafo representada por un subconjunto de vertices que solo estan conectados consigo mismos.

Parte 3: Para probar el dfs puede utilizar los archivos de distances, como por ejemplo `distances5.txt` y `distances6.txt`, que deberían retornar que hay un ciclo y dar un orden topológico respectivamente.

Parte 4: En el pdf, en el apartado casos de prueba, se explica cómo correr y probar este programa.

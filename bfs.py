# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720


import sys
import time

def bfs(matrix):
    visited = [False]*(len(matrix))
    stack = []
    answer = []
    vertex = 0
    """
    Se recorren los vertices por medio de un BFS, y para cada uno siempre que aun no se haya visitado
    se efectua el algoritmo, de esta forma para cada subconjunto se obtiene su arbol y si el grafo es 
    disconexo se abarcan los demas subconjuntos
    """
    while vertex < len(visited):
        if visited[vertex] == False:
            stack.append(vertex)
            visited[vertex] = True
            group = [vertex]
            while (len(stack)>0):
                actual = stack.pop(0) #sacar el primero del stack
                for i in range(len(matrix)): #recorrer los vertices adyacentes
                    if matrix[actual][i] > 0 and visited[i] == False: #si es adyacente y no se ha recorrido
                        visited[i] = True #se marca como visitado
                        stack.append(i) #se agrega al final del stack
                        group.append(i) #se agrega al subconjunto
            answer.append(group)
        vertex +=1
    return answer

            


matrix = []
lines=sys.stdin.readlines()
for line in lines:
    row = []
    line = line.replace("\n","").split("\t")
    for v in line:
        row.append(int(v))
    matrix.append(row)

print(bfs(matrix))

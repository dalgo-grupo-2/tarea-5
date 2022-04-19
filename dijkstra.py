# Juan Diego Yepes - 202022391]
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys
import math
import time

def dijkstra(matrix:list)->list:
    '''
    Ejecuta el algoritmo de Dijkstra desde todos los nodos base para encontrar el camino más corto 
    a todos los demás nodos.
    Retorna una matriz de costos mínimos para cada nodo de la matriz.
    '''
    #Se inicializa la matriz de costos minimos
    rowSize = len(matrix)
    colSize = len(matrix[0])
    minValues = []
    i=0
    j=0
    while i<rowSize:
        j=0
        row = []
        while j<colSize:
            if j==i:
                row.append(0)
            else:
                row.append(math.inf)
            j+=1
        minValues.append(row)
        i+=1 

    k=0
    #Se relajan los pesos del primer nodo
    while k < rowSize:
        go = True
        paths = {}
        r = 0
        mini = math.inf
        index = -1
        while r < colSize:
            value = matrix[k][r]
            if value != -1 and value !=0:
                minValues[k][r]=value
                paths[r]=(k,matrix[k][r])
                if value<mini:
                    mini=value
                    index = r
            r+=1
        #Se revisa si el nodo está conectado con algún otro
        if index != -1:
            go = True
            r=0
            paths.pop(index)
            #Se revisan los nuevos caminos a recorrer
            while r < colSize:
                value = 0
                if matrix[index][r] != -1 and matrix[index][r]!=0:
                    value = matrix[index][r]+minValues[k][index]
                    if value < minValues[k][r]:
                        if paths.get(r)!=None:
                            if value<paths[r][1]:
                                paths[r]=(index,value)
                        else:
                            paths[r]=(index,value)
                r+=1
        else:
            go = False
        #Se revisa que se hayan generado nuevos caminos
        if bool(paths)==False:
            go = False
        #Se ejecuta el algoritmo de Dijkstra hasta que ya no hayan nodos por recorrer
        while go == True:
            pathKeys = paths.keys()
            minVal = math.inf
            minPath = None
            for key in pathKeys:
                arrive = paths[key]
                if arrive[1]<minVal:
                    minPath=key
                    minVal = arrive[1]
            minValues[k][minPath]=minVal
            paths.pop(minPath)
            p=0
            while p < colSize:
                val = 0
                if matrix[minPath][p] != -1 and matrix[minPath][p] !=0:
                    val = matrix[minPath][p]+minValues[k][minPath]
                    if val < minValues[k][p]:
                        if paths.get(p)!=None:
                            if val<paths[p][1]:
                                paths[p]=(minPath,val)
                        else:
                            paths[p]=(minPath,val)
                p+=1
            if bool(paths)==False:
                go=False
        k+=1
    return minValues


matrix = []
lines=sys.stdin.readlines()
c = 0
while c<len(lines) and lines[c]!="\n":
    line = lines[c].strip().replace("\n","").split("\t")
    lineInt = []
    for value in line:
        valInt = int(value)
        lineInt.append(valInt)
    matrix.append(lineInt)
    c+=1
minValues = dijkstra(matrix)
for row in minValues:
    print(row)

'''
start_time = time.process_time()
print(dijkstra(matrix))
stop_time = time.process_time()
elapsed_time_mseg = (stop_time - start_time)*1000
print(elapsed_time_mseg)
'''
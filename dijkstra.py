# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys
import math

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
    marked = []
    i=0
    j=0
    while i<rowSize:
        j=0
        row = []
        rowMar = []
        while j<colSize:
            if j==i:
                row.append(0)
                rowMar.append(True)
            else:
                row.append(math.inf)
                rowMar.append(False)
            j+=1
        minValues.append(row)
        marked.append(rowMar)
        i+=1 

    k=0
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
        marked[k][index] = True
        r=0
        paths.pop(index)
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
        while go == True:
            pathKeys = paths.keys()
            minVal = math.inf
            minPath = None
            for key in pathKeys:
                arrive = paths[key]
                if arrive[1]<minVal:
                    minPath=key
                    minVal = arrive[1]
            marked[k][minPath]=True
            minValues[k][minPath]=minVal
            paths.pop(minPath)
            p=0
            while p < colSize:
                val = 0
                if matrix[minPath][p] != -1 and matrix[minPath][p] !=0:
                    val = matrix[minPath][p]+minValues[k][minPath]
                    if val < minValues[k][p] and marked[k][p]==False:
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
while c<len(lines):
    line = lines[c].replace("\n","").split("\t")
    lineInt = []
    for value in line:
        valInt = int(value)
        lineInt.append(valInt)
    matrix.append(lineInt)
    c+=1
print(dijkstra(matrix))
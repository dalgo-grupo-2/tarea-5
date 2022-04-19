# Juan Diego Yepes - 202022391]
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys
import math
import time

def BellmanFord(matrix:list)->list:
    '''
    Ejecuta el algoritmo de BellmanFord desde todos los nodos base para encontrar el camino más corto 
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
        #Estructura para guardar nodos de los cuales se llega
        arrivePath = {}
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
        #Se revisa que el nodo k no esté aislado
        if index != -1:
            arrivePath[index]=k
            go = True
            r=0
            paths.pop(index)
            #Se revisan los posibles caminos generados a partir del nuevo nodo agregado
            while r < colSize:
                value = 0
                if matrix[index][r] != -1 and matrix[index][r]!=0:
                    #Se toma en cuenta el peso del nuevo camino y se suma con el peso hasta ese punto
                    value = matrix[index][r]+minValues[k][index]
                    #Se revisa si este peso es menor al anterior minimo para este nodo
                    if value < minValues[k][r]:
                        #Se revisa si el nodo ya está en los posibles caminos
                        if paths.get(r)!=None:
                            #Si el nodo ya está entonces se revisa que sea menor al guardado anteriormente
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
        while go == True:
            pathKeys = paths.keys()
            minVal = math.inf
            minPath = None
            #Se selecciona el nuevo nodo a recorrer
            for key in pathKeys:
                arrive = paths[key]
                if arrive[1]<minVal:
                    minPath=key
                    minVal = arrive[1]
                    pathTo = arrive[0]
            paths.pop(minPath)
            p=0
            #Se revisa si este camino ya había sido tomado
            if arrivePath.get(minPath)!=None:
                if arrivePath[minPath] != pathTo:
                    arrivePath[minPath]=pathTo
                    minValues[k][minPath]=minVal
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
            else:
                arrivePath[minPath]=pathTo
                minValues[k][minPath]=minVal
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
while c<len(lines)and lines[c]!="\n":
    line = lines[c].strip().replace("\n","").split("\t")
    lineInt = []
    for value in line:
        valInt = int(value)
        lineInt.append(valInt)
    matrix.append(lineInt)
    c+=1
minValues = BellmanFord(matrix)
for row in minValues:
    print(row)

'''
start_time = time.process_time()
print(dijkstra(matrix))
stop_time = time.process_time()
elapsed_time_mseg = (stop_time - start_time)*1000
print(elapsed_time_mseg)
'''
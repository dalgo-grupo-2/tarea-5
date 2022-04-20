# Juan Diego Yepes - 202022391]
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys
import math
import time
from typing import ParamSpecArgs

def kruskal(matrix:list)->list:
    roads={}
    mins=[]
    sizeV = len(matrix)
    i,j,k=0,0,0
    while i < sizeV:
        j=i
        while j < sizeV:
            cost = matrix[i][j]
            if cost != 0 and cost != -1:
                roads[k]=[cost,i,j]
                mins.append(k)
                k+=1
            j+=1
        i+=1
    mins = mergeSort(mins,roads)
    partition = createPartition(sizeV)
    roadsNeeded=[]
    i=0
    while i<len(mins):
        road = mins[i]
        info = roads[road]
        startNode = info[1]
        endNode = info[2]
        if sameSubset(startNode,endNode,partition)==False:
            roadsNeeded.append(road)
            union(startNode,endNode,partition)
        i+=1
    return roadsNeeded, roads

def createPartition(sizeV:int)->dict:
    partition = {}
    i=0
    while i < sizeV:
        partition[i]={"parent":i,"height":1}
        i+=1
    return partition

def find(v:int, partition:dict)->int:
    if partition[v]["parent"]==v: #es su mismo representante (caso base)
        return v 
    s = find(partition[v]["parent"],partition) #llamado recursivo, subimos en la recursión para saber quién es la raíz
    partition[v]["parent"] = s #aplanar arbol
    return s

def sameSubset(v1:int,v2:int, partition: dict)->bool:
    return find(v1,partition)==find(v2,partition)

def union(v1:int, v2:int, partition)->None:
    s1 = find(v1,partition)
    s2 = find(v2,partition)
    if (partition[s1]["height"]<partition[s2]["height"]): #si el arbol tiene mayor altura
        partition[s1]["parent"]=s2; # pasarle el representante a apuntar al conjunto con el que queremos unirlo
    else:
        partition[s2]["parent"]=s1
        if (partition[s1]["height"] == partition[s2]["height"]):
            partition[s2]["height"] += 1; #solo se actualiza la altura del representante. (están mal calculados pero es suficiente)

def mergeSort(mins:dict,edges:dict)->list:
    #Tomado de https://www.educative.io/edpresso/merge-sort-in-python
    if len(mins) > 1:
        mid = len(mins) // 2
        left = mins[:mid]
        right = mins[mid:]

        # Recursive call on each half
        mergeSort(left,edges)
        mergeSort(right,edges)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if edges[left[i]] <= edges[right[j]]:
              # The value from the left half has been used
              mins[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                mins[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            mins[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mins[k]=right[j]
            j += 1
            k += 1
    return mins

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
answer = kruskal(matrix)
roadsNeeded = answer[0]
roads = answer[1]
for road in roadsNeeded:
    cost = roads[road][0]
    origin = roads[road][1]
    destiny = roads[road][2]
    print("Se necesita la autopista: {} que va desde el nodo {} hasta el nodo {} con un costo de {}".format(road,origin,destiny,cost))

"""
for row in minValues[0]:
    print(row,minValues[1][row])
"""
import sys
import math
import time

def kruskal(matrix:list):
    roads={}
    i,j,k=0,0,0
    while i < len(matrix):
        j=i
        while j < len(matrix):
            cost = matrix[i][j]
            if cost != 0 and cost != -1:
                roads[k]=[cost,i,j]
                k+=1
            j+=1
        i+=1

    roads = dict(sorted(list(roads.items()),key=lambda x:x[1][0]))
    partition = createPartition(len(matrix))
    roadsNeeded=[]
    for i in roads:
        start = roads[i][1]
        end = roads[i][2]
        if not sameSubset(start, end, partition):
            roadsNeeded.append(i)
            union(start, end, partition)
    print(roads)
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
    print("Se necesita la doble vía de costo {} que va desde el nodo {} hasta el nodo {} ".format(cost,origin,destiny))
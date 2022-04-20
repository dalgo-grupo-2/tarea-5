# Juan Diego Yepes - 202022391]
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import sys
import math
import time

def floydWarshall(matrix)->list:
    #Se inicializa la matriz cubica de costos minimos
    sizeV = len(matrix)
    minValues = []
    i=0
    j=0
    k=0
    while k<=sizeV:
        i=0
        matrixK = []
        while i<sizeV:
            j=0
            row = []
            while j<sizeV:
                if j==i:
                    row.append(0)
                else:
                    row.append(math.inf)
                j+=1
            matrixK.append(row)
            i+=1 
        minValues.append(matrixK)
        k+=1
    #Se reinician los contadores
    i,j,k=0,0,0
    n=sizeV
    while k<=n:
        i=0
        while i<n:
            j=0
            while j<n:
                if k == 0:
                    if matrix[i][j]!=-1 and matrix[i][j]!=0:
                        minValues[k][i][j] = matrix[i][j]
                elif k>0:
                    minValues[k][i][j] = min(minValues[k-1][i][j],minValues[k-1][i][k-1]+minValues[k-1][k-1][j])
                j+=1
            i+=1
        k+=1
    return minValues[k-1]

"""
fun floydWarshall(G(V,E,c): Graph) ret D: matrix[0,|V|)[0,|V|) of int
var m: matrix [0,|V|][0,|V|)[0,|V|) of int
var i,j,k,n: nat
k,n:=0,|V|;
do k≤n →
i:= 0
do i<n →
j:=0
do j<n →
 if k=0 → m[k,i,j] = c(i,j)
 [] k>0 → m[k,i,j] = min(m[k-1,i,j],m[k-1,i,k-1]+m[k-1,k-1,j]
 fi
 j:=j+1
od
i:=i+1
od
k:=k+1
od
"""

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
minValues = floydWarshall(matrix)
for row in minValues:
    print(row)

'''
start_time = time.process_time()
print(dijkstra(matrix))
stop_time = time.process_time()
elapsed_time_mseg = (stop_time - start_time)*1000
print(elapsed_time_mseg)
'''
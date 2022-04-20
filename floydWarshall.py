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
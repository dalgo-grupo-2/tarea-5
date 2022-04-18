# Juan Diego Yepes - 202022391
# Juan Diego Calixto - 202020774
# Sergio Pardo Gutiérrez - 202025720

import math
import sys

vertices = []
edges = []


def depthFirst(start: int):
    answer = []
    stack = []
    visited = [False]*len(vertices)
    stack.append(start)
    visited[start] = True

    while (len(stack) > 0):
        next = stack.pop()
        answer.append(vertices[next])
        for i in range(0, len(vertices)):
            if (edges[next][i] and visited[i] and i in stack):
                return True

            if (edges[next][i] and not visited[i]):
                stack.append(i)
                visited[i] = True
        
    return answer


lines=sys.stdin.readlines()
c = 0
while c<len(lines):
    line = lines[c].replace("\n","").split("\t")
    nextInt = 0
    lineEdg = []
    for value in line:
        valInt = int(value)

        if nextInt not in vertices:
            vertices.append(nextInt) # se puede hacer de forma más eficiente

        if (valInt > 0):
            lineEdg.append(True)
        else:
            lineEdg.append(False)
        
        nextInt += 1 

    edges.append(lineEdg)
    c+=1


print(depthFirst(0))

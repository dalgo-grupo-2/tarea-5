import random

def generateRandomGraphKruskal(size:int)->None:
    i=0
    j=0
    sizeI = size
    graph = []
    while i<size:
        row = []
        j=0
        while j < size:
            row.append(0)
            j+=1
        graph.append(row)
        i+=1
    i=0
    j=0
    while i<size:
        row = []
        j=i
        while j<size:
            if i==j:
                graph[i][j]=0
            else:
                number = random.randint(1,99)
                graph[i][j]=number
                graph[j][i]=number
            j+=1
        i+=1
    return graph

graph = generateRandomGraphKruskal(0)

i=0
j=0
while i < len(graph):
    line = ""
    j=0
    while j < len(graph):
        if j == len(graph)-1:
            line += str(graph[i][j])
        else:
            line+= str(graph[i][j]) + "\t"
        j+=1
    print(line)
    i+=1
import math


# vertices = [0,1,2,3,4]
# edges = [
#     [False,True,True,False,False],
#     [True,False,True,True,False],
#     [True,False,False,True,True],
#     [True,False,False,False,True],
#     [True,True,True,True,False]
#     ]

# vertices = [0,1,2]
# edges = [
#     [False,True,False],
#     [False,False,True],
#     [False,False,False]
#     ]

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


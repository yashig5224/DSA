#basic dfs code-recurisve stack approach
from asyncio import graph


def dfs(graph, u, visited):
    visited[u] = True

    print(u, end=" ")

    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited)
    #print dfs
visited = [False] * len(graph)

dfs(graph, 0, visited)        

#iterative stack approach
def dfs_iterative(graph, start):
    n = len(graph)
    visited = [False] * n

    stack = [start]
    visited[start] = True

    while stack:
        u = stack.pop()

        print(u, end=" ")

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                
                
#dfs disconnected graph
def dfs_all(graph):
    n = len(graph)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)

#dfs connected graph-outer loop changes
def dfs_all(graph):
    n = len(graph)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)                            
                
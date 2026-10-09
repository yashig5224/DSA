#bfs code
from collections import deque

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque()

    queue.append(start)
    visited[start] = True

    while queue:
        u = queue.popleft()

        print(u, end=" ")

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                
                
#bfs with graph input
from collections import deque

n = 5
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]

graph = [[] for _ in range(n)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # undirected graph
def bfs(start):
    visited = [False] * n
    q = deque([start])

    visited[start] = True

    while q:
        u = q.popleft()
        print(u, end=" ")

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)    
    
#bfs for disconnected graph
def bfs_all(graph):
    n = len(graph)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            q = deque([i])
            visited[i] = True

            while q:
                u = q.popleft()
                print(u, end=" ")

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)


#                                  
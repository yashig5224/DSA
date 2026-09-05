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
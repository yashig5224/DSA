from collections import deque

def bfs_cycle(graph, start, visited):
    q = deque()

    q.append((start, -1))
    visited[start] = True

    while q:
        u, parent = q.popleft()

        for v in graph[u]:

            # Unvisited neighbor
            if not visited[v]:
                visited[v] = True
                q.append((v, u))

            # Visited and not parent
            elif v != parent:
                return True

    return False


#disconnected graph cycle detection
def has_cycle(graph):
    n = len(graph)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            if bfs_cycle(graph, i, visited):
                return True

    return False
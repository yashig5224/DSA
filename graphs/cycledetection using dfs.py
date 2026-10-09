def dfs(graph, u, parent, visited):
    visited[u] = True

    for v in graph[u]:

        # Case 1: Unvisited neighbor
        if not visited[v]:
            if dfs(graph, v, u, visited):
                return True

        # Case 2: Visited neighbor which is not parent
        elif v != parent:
            return True

    return False


#disconnected graph cycle detection
def has_cycle(graph):
    n = len(graph)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            if dfs(graph, i, -1, visited):
                return True

    return False
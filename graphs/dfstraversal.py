#basic dfs code
def dfs(graph, u, visited):
    visited[u] = True

    print(u, end=" ")

    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited)
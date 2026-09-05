#adjacency list representation of a graph

#UNDIRECTED GRAPH
print("Undirected Graph:")
n = 5

graph = [[] for _ in range(n)]

edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3)
]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    print(i, "->", graph[i])
    
#directed graph
print("\nDirected Graph:")
n = 5

graph = [[] for _ in range(n)]

edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]

for u, v in edges:
    graph[u].append(v)

for i in range(n):
    print(i, "->", graph[i])    

#weighted graph
print("\nWeighted Graph:")
n = 4

graph = [[] for _ in range(n)]

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (1, 3, 2)
]

for u, v, weight in edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))
    
    
#adjacency matrix representation of a graph
#edge list representation of a graph

#0 based and 1 based indexing
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

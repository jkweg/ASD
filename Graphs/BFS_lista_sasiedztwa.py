# Zlozonosc O(V + E)

from collections import deque

def BFS(G,s): # s to jakis startowy punkt dla ktorego wykonujemy BFS
    n = len(G)
    Q = deque()

    d = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    return d,parent,visited

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
]

results = BFS(G,0)
print(results)
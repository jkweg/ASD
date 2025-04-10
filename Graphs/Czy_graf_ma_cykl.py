# Sprawdzamy czy podany graf ma cykl , za pomoca DFS

from collections import deque

def czy_ma_cykl(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFScycle(u,parent):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                if DFScycle(v,u):
                    return True
            elif v != parent:
                return True
        return False

    for v in range(n):
        if not visited[v]:
            if DFScycle(v,None):
                return True
    return False

Graph1 = [
    [],
    [2, 3],
    [1, 2],
    [1, 3]
]
print(czy_ma_cykl(Graph1))

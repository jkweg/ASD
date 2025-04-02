from collections import deque

def czy_dwudzielny(G):
    n = len(G)
    Q = deque()
    colors = [0 for _ in range(n)]

    for i in range(n):
        if colors[i] == 0:
            Q.append(i)
            colors[i] = 1

            while len(Q) > 0:
                u = Q.popleft()
                for v in G[u]:
                    if colors[v] == 0:
                        colors[v] = -1*colors[u]
                        Q.append(v)
                    elif colors[v] == colors[u]:
                        return False
    return True

Graph1 = [
    [],
    [2, 3],
    [1, 2],
    [1, 3]
]
Graph2 = [
    [2,3],
    [2,3],
    [0,1],
    [0,1]
]
# Graf 1 nie jest dwudzielny , Graf 2 jest dwudzielny
print(czy_dwudzielny(Graph1))
print(czy_dwudzielny(Graph2))
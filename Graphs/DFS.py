def DFS(G):
    t = 0
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [0] * n
    przet = [0] * n
    def DFSvisit(G,v):
        nonlocal t
        visited[v] = True
        t += 1
        d[v] = t
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFSvisit(G,u)
        t+=1
        przet[v] = t
    for i in range(n):
        if not visited[i]:
            DFSvisit(G,i)
    return visited,parent,d,przet






G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
]
vis,par,odkrycie,przetworzenie = DFS(G)
print(vis)
print(par)
print(odkrycie)
print(przetworzenie)
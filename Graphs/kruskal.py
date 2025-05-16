# Algorytm znajdujacy MST ( minimalne drzewo rozpinajace )

# Zloznosc ElogV lub Elog*V , gdzie log* ,to logarytm iterowany

def list_to_edges(G):
    E = []
    n = len(G)
    for u in range(n):
        for v , w in G[u]:
            if u <  v:
                E.append((u,v,w))
    return E

def kruskal(G):
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0] * n
    MST = []

    E = list_to_edges(G)
    E.sort(key = lambda x:x[2]) # sortuje po 2 elemencie

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(x,y):
        x = find(x)
        y = find(y)

        if x == y: return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    for u , v , w in E:
        if find(u) != find(v):
            union(u,v)
            MST.append((u,v,w))
            if len(MST) == n - 1:
                break
    return MST

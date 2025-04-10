# Szukamy sciezki hamiltona w grafie skierowanym
# Sortujemy wierzcholki topologicznie i sprawdzamy czy mozna przejs od lewej do prawej po kolejnych krawedziach

def sort_top(G):
    n = len(G)
    visited = [False] * n
    res = []

    def dfsvisit(G,v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfsvisit(G,u)
        res.append(v)

    for i in range(n):
        if not visited[i]:
            dfsvisit(G,i)

    return res[::-1]

def sciezka_HAM(G):
    A = sort_top(G)
    n = len(G)
    for i in range(n-1):
        if A[i+1] not in G[A[i]]:
            print(A[i])
            return False
    return True

G = [
    [1, 2],
    [3],
    [3, 4, 5],
    [],
    [5],
    [],
]
print(sciezka_HAM(G))
print(sort_top(G))
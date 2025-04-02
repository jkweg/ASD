def ile_spoj_sklad(G): # Stosujemy algorytm DFS z paroma dodatkami
    n = len(G)
    cnt = 0
    visited = [False for _ in range(n)]

    def DFSvisit(G,u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSvisit(G,v)
    for u in range(n):
        if not visited[u]:
            cnt+=1
            DFSvisit(G,u)
            #print(visited)
    return cnt




# Implementujemy graf jako liste sasiedztwa
Graph = [
    [1, 2],    # 0 <- wierzcholek , Przyklad: Istnieją krawedzie 0 -> 1 , 0 -> 2
    [3],       # 1
    [3, 4, 5], # 2
    [],        # 3
    [5],       # 4
    [],        # 5
    [7],       # 6
    []         # 7
]

graf2 = [[1],
         [2],
         [3],
         [0]]
print(ile_spoj_sklad(Graph))
print(ile_spoj_sklad(graf2))









#1 wykonujemy DFS i zaposujemy czasy przetworzenia
#2 odwracamy krawedzie
#3 wykonujemt ponownie DFS ale po malejacych czasach przetworzenia

def strongly_coherent_comps(G):

    n = len(G)
    visited = [False] * n
    times = [0]*n
    t = 0

    def DFS1(G,v):
        nonlocal t
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                DFS1(G,u)
        times[v] = t
        t += 1

    for v in range(n):
        if not visited[v]:
            DFS1(G,v)

    reversed_G = [[] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            reversed_G[u].append(v)

    vertex_time = [(times[v],v) for v in range(n)]
    vertex_time.sort(reverse = True)

    visited = [False] * n
    components = []
    def DFS2(G,v,comp):
        visited[v] = True
        comp.append(v)
        for u in reversed_G[v]:
            if not visited[u]:
                DFS2(G,u,comp)


    for _,v in vertex_time:
        if not visited[v]:
            comp = []
            DFS2(G,v,comp)
            components.append(comp)

    return components

graph = [
    [1],
    [2],
    [0, 3],
    [4],
    []
]

print(strongly_coherent_comps(graph))


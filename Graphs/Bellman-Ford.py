# Lista sasiedzwta G[u] = (v,w)

def bellman_ford(G,s):
    n = len(G)
    d = [float('inf')] * n
    parents = [None] * n

    d[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v,w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parents[v] = u

    # Weryfikacja czy jest cykl o ujemnej wartosci

    for u in range(n):
        for v,w in G[u]:
            if d[v] > d[u] + w:
                return None

    return d , parents

def path(parents,v):
    path = []
    while v is not None:
        path.append(v)
        v = parents[v]
    return path[::-1]


graph = [
        [(1,4),(4,2)],
        [(0,4),(2,1),(4,1)],
        [(1,1),(4,3),(3,2)],
        [(2,2),(5,7)],
        [(0,2),(1,1),(2,3),(5,6)],
        [(4,6),(3,7)]
        ]

d , p = bellman_ford(graph,0)
print(d)
print(p)
for v in range(len(graph)):
    pth = path(p,v)
    print(pth)
from queue import PriorityQueue
# dijkstra przyjmujaca graf jako macierz wag

def ad_list_to_macierz(G):
    n = len(G)
    M = [[float('inf')]* n for _ in range(n)]
    i = 0
    while i < n:
        for u,w in G[i]:
            M[i][u] = w
        i+= 1
    return M

def dijkstra(G,s):
    n = len(G)
    d = [float('inf')]*n
    d[s] = 0

    pq = PriorityQueue()
    pq.put((0,s)) #koszt , wierzcholek

    while not pq.empty():
        current_cost , u = pq.get()
        if current_cost > d[u]:
            continue
        for i in range(n):
            if G[u][i] != float('inf'):
                w = G[u][i]
                c = d[u] + w
                if d[i] > c:
                    d[i] = c
                    pq.put((c,i))
    return d

graph = [
        [(1,4),(4,2)],
        [(0,4),(2,1),(4,1)],
        [(1,1),(4,3),(3,2)],
        [(2,2),(5,7)],
        [(0,2),(1,1),(2,3),(5,6)],
        [(4,6),(3,7)]
        ]
"""W = ad_list_to_macierz(graph)
for row in W:
    print(row)"""
M = ad_list_to_macierz(graph)
d = dijkstra(M,0)
print(d)




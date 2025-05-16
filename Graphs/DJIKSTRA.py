# Algorytm szukania najkrotszych sciezek w grafach wazonych
# Wagi musza byc NIEUJEMNE , inaczej nie dziala

from queue import PriorityQueue


def dijkstra(G,s):
    n = len(G)
    distances = [float('inf')] * n
    parents = [None] * n

    pq = PriorityQueue() # pusta kolejka priorytetowa
    pq.put((0,s))
    distances[s] = 0

    while not pq.empty():
        current_dist , u = pq.get()
        if current_dist > distances[u]:
            continue

        for v,w in G[u]:
            c = distances[u] + w
            if distances[v] > c:
                distances[v] = c
                parents[v] = u
                pq.put((c,v))

    return distances,parents

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

d , p = dijkstra(graph,0)
print(d)
print(p)
for v in range(len(graph)):
    pth = path(p,v)
    print(pth)
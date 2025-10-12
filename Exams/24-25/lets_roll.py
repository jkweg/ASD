from kol2testy import runtests
from queue import PriorityQueue
from heapq import heappop , heappush

# JAKUB WĘGRZYNIAK   

def edges_to_ad_list(E):
    n = -1
    for u,v,_ in E:
        n = max(n,u,v)
    n+= 1

    G = [[] for _ in range(n)]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    return G


def lets_roll(start_city, flights, resorts):
    G = edges_to_ad_list(flights)
    n = len(G)

    is_resort = [False] * n
    visited_resorts = [False] *n

    for r in resorts:
        is_resort[r] = True
    
    d = [float('inf')] * n
    d[start_city] = 0

    pq = PriorityQueue()
    pq.put((0,start_city))

    total = 0

    while not pq.empty():
        cost , u = pq.get()
        
        if visited_resorts[u] or cost > d[u]:
            continue

        if is_resort[u] and not visited_resorts[u]:
            visited_resorts[u] = True
            total += 2 * d[u]
            continue
        
        for v , w in G[u]:
            if not visited_resorts[v]:
                c = d[u] + w
                if d[v] > c:
                    d[v] = c
                    pq.put((c,v))
    
    return total
    
# Wzorcowka ^ ElogV

runtests(lets_roll, all_tests = True)

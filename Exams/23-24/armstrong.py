from egz1atesty import runtests
from queue import PriorityQueue

def edges_to_adj_list(E):
  n = -1

  for u , v , _ in E:
    n = max(n,u,v)

  n+= 1

  G = [[] for _ in range(n)]

  for u , v , w in E:
    G[u].append((v,w))
    G[v].append((u,w))
  return G

def edges_to_matrix(E):
  n = -1

  for u , v , _ in E:
    n = max(n,u,v)
  
  n += 1

  G = [[float('inf')]*n for _ in range(n)]

  for i in range(n):
    G[i][i] = 0 

  for u , v , w in E:
    G[u][v] = w
    G[v][u] = w
  return G

#  Wersja V^3 ( za 1.0 pkt)

# def Floyd_Warshall(G):

#   n = len(G)

#   d = [row[:] for row in G]

#   for k in range(n):
#     for x in range(n):
#       for y in range(n):
#         s = d[x][k] + d[k][y]
#         if s < d[x][y]:
#           d[x][y] = s
  
#   return d

# def armstrong( B, G, s, t):
#   G = edges_to_matrix(G)

#   dist = Floyd_Warshall(G)

#   min_d = dist[s][t]

#   for i , p , q in B:
#     if dist[s][i] != float('inf') and dist[i][t] != float('inf'):
#       new_dist = dist[s][i] + (dist[i][t] * p)//q
#       min_d = min(min_d , new_dist)
  
#   return min_d

# WZORCOWKA

# def armstrong( B, G, s, t):
#   G = edges_to_adj_list(G)
#   n = len(G)

#   bikes = [None] * n
#   for i , p , q in B:
#     if bikes[i] is None or p/q < bikes[i]:
#       bikes[i] = p/q


#   d = [[float('inf'),float('inf')] for _ in range(n)]
#   d[s][0] = 0

#   pq = PriorityQueue()
#   pq.put((0,s,0,1.0))   #(koszt , wierzcholek , has_bike , predkosc) Jak has_bike == 0 to nie mamy roweru

#   while not pq.empty():

#     cost , u , has_bike , ratio = pq.get()

#     if u == t:
#       return int(cost)

#     if cost > d[u][has_bike]:
#       continue

#     if has_bike == 0:
#       r = bikes[u]
#       if r is not None and cost < d[u][1]:
#         d[u][1] = cost
#         pq.put((cost,u,1,r))
      
#       for v , w in G[u]:
#         new_c = cost + w
#         if d[v][0] > new_c:
#           d[v][0] = new_c
#           pq.put((new_c,v,0,1.0))
    
#     else:
#       for v , w in G[u]:
#         c = cost + w * ratio
#         if c < d[v][1]:
#           d[v][1] = c
#           pq.put((c,v,1,ratio))
  
#   return None


# Wzorcowka 2

def dijkstra(G,s):
  n = len(G)

  d = [float('inf')] * n
  d[s] = 0

  pq = PriorityQueue()
  pq.put((0,s))

  while not pq.empty():

    cost , u  = pq.get()

    if cost > d[u]:
      continue
      
    for v , w in G[u]:
      c = cost + w
      if d[v] > c:
        d[v] = c
        pq.put((c,v))

  return d


def armstrong( B, G, s, t):
  G  = edges_to_adj_list(G)

  dist = dijkstra(G,s)
  dist2 = dijkstra(G,t)

  mini = dist[t]

  for i , p , q in B:
    new_dist = dist[i] + (p/q) * dist2[i]
    mini = min(mini , new_dist)
  
  return int(mini)
  
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True)


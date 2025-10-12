from egz2btesty import runtests
from queue import PriorityQueue
from collections import deque
def edges_to_adj(E):

  n = -1
  for u , v , _ , _  in E:
    n = max(n,u,v)
  n += 1

  G = [[] for _ in range(n)]

  for u , v , w , type in E:
    G[u].append((v,w,type))
    G[v].append((u,w,type))
  
  return G

def modi_dijkstra(G,s,t):
  n = len(G)
  dist = [[float('inf'),float('inf')] for _ in range(n)]  #d[i][0] - minimalny do i konczac indyjska , d[i][1] - konczac przyladkowa
  
  dist[s][0] = 0
  dist[s][1] = 0

  pq = PriorityQueue()
  pq.put((0,s,None)) # koszt , wierzcholek , typ poprzedni

  while not pq.empty():

    cost , u , typ = pq.get()

    if u == t:
      return cost

    if typ is None:
      for v , w , new_type in G[u]:
        if new_type == 'I':
          dist[v][0] = w
          pq.put((w,v,new_type))
        else:
          dist[v][1] = w
          pq.put((w,v,new_type))
    if typ == 'I':
      for v, w , new_type in G[u]:
        if new_type == typ:
          c = cost + w + 5
          if dist[v][0] > c:
            dist[v][0] = c
            pq.put((c,v,new_type))
        else:
          c = cost + w + 20
          if dist[v][1] > c:
            dist[v][1] = c
            pq.put((c,v,new_type))
    if typ == 'P':
      for v , w , new_type in G[u]:
        if new_type == typ:
          c = cost + w + 10
          if dist[v][1] > c:
            dist[v][1] = c
            pq.put((c,v,new_type))
        else:
          c = cost + w + 20
          if dist[v][0] > c:
            dist[v][0] = c
            pq.put((c,v,new_type))

  return -1

def dijkstra(G,s,t):

  n = len(G)
  dist = [[float('inf'), float('inf')] for _ in range(n)]
  dist[s][0] = dist[s][1] = 0

  pq = PriorityQueue()
  pq.put((0, s, None))


  while not pq.empty():
    cost , u , typ = pq.get()

    if typ is not None:
      idx = 0 if typ == 'I' else 1
      if cost > dist[u][idx]:
        continue
    
    if u == t:
      return cost
    
    for v , w , new_typ in G[u]:
      if typ is None:
        penalty = 0
      elif typ == 'I' and new_typ == 'I':
        penalty = 5
      elif typ == 'P' and new_typ == 'P':
        penalty = 10
      else:
        penalty = 20
      

      idx = 0 if new_typ == 'I' else 1

      c = cost + w + penalty
      if dist[v][idx] > c:
        dist[v][idx] = c
        pq.put((c,v,new_typ))
      
  return -1


def tory_amos( E, A, B ):
  G = edges_to_adj(E)
  dist = dijkstra(G,A,B)

  return dist

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )

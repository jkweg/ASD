from egz3atesty import runtests
from collections import deque
# Wzorcowka: 4.0 pkt
def mykoryza( G,T,d ):
  n = len(G)
  owner = [None] * n
  dist = [float('inf')] * n

  dq = deque()

  idx = 0
  for grzyb in T:
    owner[grzyb] = idx
    dist[grzyb] = 0
    dq.append((grzyb,idx))
    idx += 1

  while dq:
    u , mush = dq.popleft()

    for v in G[u]:
      if owner[v] is None:
        owner[v] = mush
        dq.append((v,mush))
        dist[v] = dist[u] + 1
      else:
        if dist[v] > dist[u] + 1:
          dist[v] = dist[u] + 1
          owner[v] = mush
          dq.append((v,mush))
        elif dist[v] == dist[u] + 1:
          if mush < owner[v]:
            owner[v] = mush
            dq.append((v,mush))
  
  cnt = 0

  for own in owner:
    if own  == d:
      cnt += 1

  return cnt

# Zlozonosc V^3 1.0 pkt
def mykoryza2( G,T,d2 ):
  n = len(G)
  d = [[float('inf')]*n for _ in range(n)]

  for u in range(n):
    d[u][u] = 0
    for v in G[u]:
      d[u][v] = 1
      d[v][u] = 1
  
  for k in range(n):
    for x in range(n):
      for y in range(n):
        s = d[x][k] + d[k][y]
        if s <d[x][y]:
          d[x][y] = s
  
  best_dist = [float('inf')] * n
  owner     = [None] * n
  idx       = 0

  for tree in T:
    for i in range(n):
        dist_i = d[tree][i]
        if dist_i < best_dist[i] or (dist_i == best_dist[i] and idx < owner[i]):
            best_dist[i] = dist_i
            owner[i]     = idx
    idx += 1


  
  cnt = 0

  for own in owner:
    if own == d2:
      cnt += 1
  
  return cnt

#Zlozonosc VE 2.0 pkt
def mykoryza3(G, T, target_id):
    n = len(G)

    def BFS(G, s):
        n = len(G)
        visited = [False] * n
        dist = [float('inf')] * n

        dist[s] = 0
        visited[s] = True

        dq = deque()
        dq.append(s)

        while dq:
            u = dq.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    dq.append(v)
        return dist

    dist_list = [None] * len(T)
    for idx, tree in enumerate(T):
        dist_list[idx] = BFS(G, tree)

    best_dist = [float('inf')] * n
    owner = [None] * n

    for idx in range(len(T)):
        for i in range(n):
            dist_i = dist_list[idx][i]
            if dist_i < best_dist[i] or (dist_i == best_dist[i] and idx < owner[i]):
                best_dist[i] = dist_i
                owner[i] = idx

    cnt = sum(1 for own in owner if own == target_id)
    return cnt
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza2, all_tests = True)

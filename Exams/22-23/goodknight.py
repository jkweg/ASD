from egz3atesty import runtests
from queue import PriorityQueue
def goodknight( G, s, t ):
  n = len(G)
  
  dist = [[float('inf')] * 17 for _ in range(n)]
  dist[s][0] = 0

  pq = PriorityQueue()
  pq.put((0,s,0)) # koszt , wierzcholek , zmeczenie

  while not pq.empty():

    cost , u , time = pq.get()

    if cost > dist[u][time]: continue

    if u == t:
       return cost

    for v in range(n):
      w = G[u][v]
      if w != -1:
        new_time = time + w
        if new_time >16:
          new_time = w
          w += 8
        
        c = cost + w
        if dist[v][new_time] > c:
          dist[v][new_time] = c
          pq.put((c,v,new_time))
  
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

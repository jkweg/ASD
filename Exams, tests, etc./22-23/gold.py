from egz1Atesty import runtests
from queue import PriorityQueue

# Wzorcowka1

def gold(G,V,s,t,r):
  n = len(G)
  infi = float('inf')
  dist = [[infi,infi] for _ in range(n)]
  # dist[i][k] - minimalny koszt dotarcia do i-tego zamku , k = 0 jeszcze nie napadlismy , k = 1 napadlismy
  dist[s][0] = 0
  dist[s][1] = -V[s]

  pq = PriorityQueue()
  pq.put((0,s,0)) # koszt , zamek , czy napadlismy 0 - nie , 1 - tak
  pq.put((-V[s] , s , 1))

  while not pq.empty():
    cost , u , robbed = pq.get()

    if cost> dist[u][robbed]:
      continue

    for v , w in G[u]:
      if robbed == 0: # mozemy obrabowac , albo isc dalej bez obrabywania

        # bez obrabowywania
        c = cost + w
        if c < dist[v][0]:
          dist[v][0] = c
          pq.put((c,v,0))
        
        # obrabowywujemy

        c2 = cost + w - V[v]
        if c2 < dist[v][1]:
          dist[v][1] = c2
          pq.put((c2,v,1))
      
      elif robbed == 1:
        # musimy isc po prostu dalej , nie ma innej opcji
        c = cost + 2 * w + r
        if c < dist[v][1]:
          dist[v][1] = c
          pq.put((c,v,1))
  
  best = min(dist[t])

  return best if best < infi else -1

# Wzorcowka 2
def dijkstra(G,s,r):
  n = len(G)
  dist = [float('inf')] * n
  pq = PriorityQueue()
  pq.put((0,s))
  dist[s] = 0
  while not pq.empty():
    cost , u = pq.get()

    for v , w in G[u]:

      if r is None:
        c = cost + w
        if c < dist[v]:
          dist[v] = c
          pq.put((c,v))
      else:
        c = cost + w * 2 + r
        if c < dist[v]:
          dist[v] = c
          pq.put((c,v))
    
  return dist
def gold2(G,V,s,t,r):
  n = len(G)
  dist1 = dijkstra(G,s,None)
  dist2 = dijkstra(G,t,r)

  mini = float('inf')

  for i in range(n):
    cost = dist1[i] + dist2[i] - V[i]
    mini = min(mini,cost)
  
  return mini


# Ta gorsza zlozonosc V*ElogV , 2.0 pkt

def gold3(G,V,s,t,r):
  n = len(G)
  mini = float('inf')
  for i in range(n):
    dist1 = dijkstra(G,s,None)
    dist2 = dijkstra(G,t,r)

    curr = dist1[i] + dist2[i] - V[i]
    mini = min(curr,mini)
  
  return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )

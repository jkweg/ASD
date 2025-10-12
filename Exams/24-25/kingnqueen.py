from egz2Atesty import runtests
from collections import deque

# Jakub Węgrzyniak

# Mój algorytm wykonuje najprostsze podejście , a dokładniej wykonuje D razy BFS. 
# Za każdym razem startuje od wierzchołka w którym jest król i sprawdzam czy jestem w stanie dotrzeć
# do miejsca gdzie jest królowa , bez przejeżdzania przez aktualnie atakowane przez bajtocje miasto.
# Na końcu zwracam ile przesyłek udało się dostarczyć.

# Zlożoność:  O( D(V+E) )


def kingnqueen( V,E,D,K,Q,B ):
  
  G = [[] for _ in range(V)]

  for u , v in E:
    G[u].append(v)
    G[v].append(u)
  
  def BFS(s,attacked,t): # attacked - czyli tam gdzie jest prowadzona dywersja
    visited = [False for _ in range(V)]
    visited[s] = True

    dq = deque()
    dq.append(s)

    while dq:

      u = dq.popleft()
      if u == t:
        return True
      for v in G[u]:
        if v != attacked and not visited[v]:  # nie przechodze do aktualnie atakowanego miasta
          visited[v] = True
          dq.append(v)

    return visited[t]
  
  cnt = 0

  for i in range(D):
    king = K[i]
    queen = Q[i]
    attack = B[i]

    if BFS(king,attack,queen):  # Sprawdzam , czy udało sie dostarczyć przesyłke
      cnt += 1
    
  return cnt
      
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kingnqueen, all_tests = True )

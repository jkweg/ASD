from collections import deque
from egz1Btesty import runtests

# Jakub Węgrzyniak

# Pomysl:
# Moj algorytm wykonuje E razy algorytm BFS , za kazdym razem podczas przechodzenia przez
# graf pomijam jedna z krawedzi(delegacji u--->v),
# a nastepnie sprawdzam czy od wierzcholka u mozna dojsc do v , czyli czy
# mozna inna droga oddac zadanie do realizacji
# Jezeli sie nie da to znaczy ze dana delegacja jest krytyczna i zwiekszam counter,
# ktory pod koniec zwracam jako finalny wynik

# Zlozonosc E*(V+E) = EV + E^2

def BFS(G,x,y):
    n = len(G)
    Q = deque()

    d = [float('inf') for _ in range(n)]
    visited  = [False for _ in range (n)]
    parents = [None for _ in range(n)]

    d[x] = 0
    visited[x] = True
    Q.append(x)

    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if u == x and v == y:
                continue
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.append(v)

    # Sprawdzamy czy mozemy dojsc z wierzcholka x do y ( czy istnieje delegacja )

    if not visited[y]:
        return True
    else:
        return False

def edges_to_graph(V,E):
    n = V
    G = [[] for _ in range(n)]

    for u , v in E:
        G[u].append(v)
    return G

def critical2(V, E):

    # e = len(E)
    G = edges_to_graph(V,E)
    cnt = 0

    for u , v in E:
        if BFS(G,u,v):
            cnt += 1

    return cnt

# ^^^ Zlozonosc najgorsza EV + E^2

def floyd_warshall(G):
    n = len(G)
    d = [row[:] for row in G]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                s = d[x][k] + d[k][y]
                if s < d[x][y]:
                    d[x][y] = s
    
    return d

def critical(V, E):

    Matrix  = [[float('inf')]*V for _ in range(V)]

    for u , v in E:
        Matrix[u][v] = -1
    
    d = floyd_warshall(Matrix)   # Jezeli droga od u do v jest mniejsza od -1 to znaczy ze da isc inaczej niz tylko ta krawedzia
    
    cnt = 0
    for u , v in E:
        if d[u][v] == -1:
            cnt += 1
    
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

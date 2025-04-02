# Zadanie:
# Sprawdzic czy istnieje sciezka od x do y , ktorej wagi sa w porzadku malejacym,
# graf dany jakos lista krawdzezi i ich wag

def check(E,x,y):
    n = 0
    for u,w,_ in E:
        n = max(n,u,w)
    n+=1 # n - ilosc wierzcholkow

    G = [[] for _ in range(n)]
    visited_e = [False for _ in range(len(E))] # len(G) ilosc krawedzi

    i = 0
    # tworzymy liste sasiedztwa zeby bylo prosciej
    for u,v,w in E:
        G[u].append((v,w,i))
        G[v].append((u,w,i))
        i+= 1

    def DFSvisit(G,u,prev,y):
        if u == y:
            return True

        for v,w,i in G[u]:
            if not visited_e[i] and w < prev:
                visited_e[i] = True
                if DFSvisit(G,v,w,y):
                    return True
        return False

    return DFSvisit(G,x,float('inf'),y)



E = [(0, 1, 3), (1, 2, 2), (2, 5, 11), (5, 6, 15), (6, 8, 12), (7, 8, 4), (0, 7, 30), (0, 3, 10),
     (1, 3, 6), (1, 4, 1), (3, 4, 17), (2, 4, 9), (4, 5, 10), (7, 3, 22), (3, 8, 7), (8, 5, 8)]

print(check(E,0,4))
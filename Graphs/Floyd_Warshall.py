# Oplacalny dla postaci macierzowej
# Dla listy sasiedztwa bardziej oplaca sie wykonac V razy djikstre albo belmana_forda

# Zlozonosc V^3

def floyd_warshall(G):
    n = len(G)
    d = [row[:] for row in G]
    print(*d,sep = '\n')
    p = [[i if d[i][j] != float('inf') else None for j in range(n)] for i in range(n)]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                 s = d[x][k] + d[k][y]
                 if s < d[x][y]:
                     d[x][y] = s
                     p[x][y] = p[k][y]

    return d, p


i = float('inf')
G = [# 0, 1, 2, 3, 4
      [0, -4,i, i, i], #0
      [i, 0, 4, 5, i], #1
      [i, i, 0, 2, i], #2
      [i, i, i, 0, 3], #3
      [i, i, i, i, 0], #4
]

dist , par = floyd_warshall(G)

print(*dist, sep = '\n')
print()
print(*par, sep = '\n')
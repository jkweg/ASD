

def find_cycle(G):
    g = [list(u) for u in G]
    cycle = []

    def dfs(v):
        for u in g[v]:
            g[v].remove(u)
            g[u].remove(v)
            dfs(u)
        cycle.append(v)
    start = None
    for i in range(len(G)):
        if G[i]:
            start = i
            break

    dfs(start)
    for j in range(len(G)):
        if len(g[j]) > 0:
            return None
    return cycle

G = [
    [1,3],
    [0,3],
    [3,4],
    [0,1,2,4],
    [2,3]
]
print(find_cycle(G))
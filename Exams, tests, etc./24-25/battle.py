from egz1Atesty import runtests
# Jakub Węgrzyniak
# Pomysl:

# Idziemy po kolei i jak natrafimy na procesor to przyporzadkowywujemy mu najblizsza katapulte po lewej


def battle(P, K, R):
    n = len(K)
    m = len(P)

    maxi = 4*(n+m) + 1

    T = [0] * maxi

    for i in range(n):
        pos = K[i]
        ran = R[i]
        T[pos] = pos + ran
    
    for i in range(m):
        pos = P[i]
        T[pos] = 'P'
    
    cnt = 0
    for i in range(maxi):
        if T[i] == 'P':
            for j in range(i-1,-1,-1):
                if T[j] != 'P' and T[j] >= i:
                    cnt += 1
                    T[j] = 0
                    break
    
    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True)

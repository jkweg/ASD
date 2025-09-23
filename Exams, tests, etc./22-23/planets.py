from egz1btesty import runtests

def planets( D, C, T, E ):
    # F[i][j] - minimalny koszt dotarca na i-ta planete majac j - ton paliwa

    n = len(D)
    F = [[float('inf')] * (E+1) for _ in range(n)]

    
    for e in range(E+1):
        F[0][e] = e * C[0]

    F[T[0][0]][0] = min(F[T[0][0]][0]  , F[0][0] + T[0][1])

    for i in range(n-1):
        dist = D[i+1] - D[i]

        # nie tankujemy
        for e in range(E+1):
            if e >= dist:
                F[i+1][e-dist] = min(F[i+1][e-dist] , F[i][e])
        
        # tankujemy
        for e in range(E+1):
            F[i+1][e] = min(F[i+1][e] , F[i+1][e-1] + C[i+1])
        
        dest , cost = T[i]
        if dest != i:
            F[dest][0] = min(F[dest][0] , F[i][0] + cost)
    
    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

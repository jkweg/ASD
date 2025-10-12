from kol3testy import runtests

def parkiet(B, C, s):
    m = len(B)
    n = len(B[0])

    F = [[float('inf')] * (n+1) for _ in range(m+1)]
    # F[i][j] - minimalna liczba ciec jaka trzeba wykonac aby miec blat [i][j]


    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            widht = m - i
            height = n - j
            sum_s = C[i][j]

            if (widht == 1 or height == 1) and sum_s <= s:
                F[i][j] = 0
                continue

            h = 0
            if i + 1 < m:
                h = C[i+1][j]
            sum_row = sum_s - h
            if sum_row <= s:
                F[i][j] = min(F[i][j] , F[i+1][j] + 1)
            
            w = 0
            if j + 1 < n:
                w = C[i][j+1]
            sum_col = sum_s - w
            if sum_col <= s:
                F[i][j] = min(F[i][j] , F[i][j+1] + 1)
    
    return F[0][0] if F[0][0] != float('inf') else -1
            
            




runtests(parkiet, all_tests = True)
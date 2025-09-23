from egz1btesty import runtests

# Zlozonosc najgorsza n^3 logn tak zwany brute
def kstrong2( T, k):
  n = len(T)

  tmp = []
  maxi = -float('inf')
  for i in range(n):
    for j in range(i,n+1):
      tmp = T[i:j]
      tmp.sort()

      for p in range(0,k+1):
        if j - i + p > 0: 
          tmp2 = tmp[p:j]
          # print(tmp2)
          maxi = max(maxi , sum(tmp2))
  
  return maxi


# WZORCOWKA

def kstrong( T, k):
    n = len(T)

    # F[i][j] = Maksymalna suma do - i-tego elementu usuwajac dokladnie j elementow

    F = [[-float('inf')] * (k+1) for _ in range(n)]

    F[0][0] = T[0]
    if k > 0:
        F[0][1] = 0

    maxi = -float('inf')

    for i in range(1,n):
        for j in range(k+1):
          if j - 1 >= 0:
            F[i][j] = max(F[i][j] , F[i-1][j-1]) # usuwamy

          F[i][j] = max(F[i][j] , F[i-1][j] + T[i],T[i])
          maxi = max(maxi,F[i][j])

    # for i in range(n):
    #    for j in range(k+1):
    #       maxi = max(maxi,F[i][j])
    
    return maxi
            

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )

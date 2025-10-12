from egz2atesty import runtests

# Zlozonosc n^2
def dominance(P):
  n = len(P)
  P.sort(key = lambda x: -x[0])
  maxi = 0

  for i in range(n):
    xi , yi = P[i]
    cnt = 0
    for j in range(i+1,n):
      xj , yj = P[j]
      if xi > xj and yi > yj:
        cnt += 1
    
    maxi = max(maxi,cnt)
  return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

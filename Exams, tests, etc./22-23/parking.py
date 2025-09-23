from egz2btesty import runtests

# Wzorcowka 4.0 pkt

def parking(X,Y):
  # F[i][j] - minimalna suma odleglosci biurowcow z do i, do przydzielonych im dzialek przy zalozeniu
  # ze biurowiec z pozycji X[i] ma przydzielona dzialke z pozycji Y[j]

  n = len(X)
  m = len(Y)

  F = [[float('inf')]*(m+1) for _ in range(n+1)]

  for j in range(m+1):
    F[0][j] = 0


  for i in range(1,n+1):
    j_min = i
    j_max = m - (n-i)
    for j in range(j_min , j_max + 1):
      best = F[i][j-1] if j > j_min else float('inf')

      cost = F[i-1][j-1] + abs(X[i-1] - Y[j-1])

      F[i][j] = min(best,cost)
  
  return F[n][m]

# Zlozonosc nm^2 , chyba 3.0pkt albo 2.0pkt
def parking2(X,Y):
  n , m  = len(X) , len(Y)

  F = [[float('inf')] * (m+1) for _ in range(n)]

  for j in range(m):
    F[0][j+1] = abs(X[0] - Y[j])

  
  for i in range(1,n):
    for j in range(i,m):
      for k in range(i-1,j):

        curr = F[i-1][k+1] + abs(X[i] - Y[j])

        if curr < F[i][j+1]:
          F[i][j+1] = curr
  
  return min(F[n-1][1:m+1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking , all_tests = True)



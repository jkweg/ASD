from egz3btesty import runtests

def uncool( P ):
  n = len(P)

  # P.sort(key = lambda x:x[0])

  for i in range(n):
    for j in range(n):
      if i != j:
        xi , yi = P[i]
        xj , yj = P[j]

        if not (xi >= xj and yi <= yj or xi <= xj and yi >= yj or xi >= xj and xi >= yj or yi <= xj and yi <= yj):
          return (i,j)
  
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True)

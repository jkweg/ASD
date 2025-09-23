from egz3btesty import runtests

# Zlozonosc O(n^2) , 1.0pkt
def kunlucky(T, k):
  n = len(T)
  kset = set()
  kset.add(k)

  x1 = k
  i = 0
  maxi = max(T) + 1
  while x1 < maxi:
    i+= 1
    x1 = x1 + (x1%i)+7
    kset.add(x1)
  
  maxi = -1
  for i in range(n):
    kcnt = 0
    cnt = 0
    for j in range(i,n):
      if T[j] in kset:
        kcnt += 1
      if kcnt > 2:
        break
      cnt += 1
      maxi = max(maxi,cnt)
  
  return maxi

# Wzorcowka O(n) 4.0pkt
def kunlucky2(T, k):
  n = len(T)
  kset = set()
  kset.add(k)

  x1 = k
  i = 0
  maxi = max(T) + 1
  while x1 < maxi:
    i+= 1
    x1 = x1 + (x1%i)+7
    kset.add(x1)
  
  left = 0
  maxi = -1
  kcnt = 0
  cnt = 0

  for right in range(n):
    if T[right] in kset:
      kcnt += 1
    
    while kcnt > 2:
      if T[left] in kset:
        kcnt -= 1
      left += 1
    
    curr_l = right - left + 1
    maxi = max(maxi,curr_l)
  
  return maxi



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky2, all_tests = True)

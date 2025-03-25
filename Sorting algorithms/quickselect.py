# Mamy tablice A i chcemy znalezc element ktory bedzie na k-tej pozycji po posortowaniu w czasie liniowym O(n)

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1] , A[r]  =A[r] ,A[i+1]
    return i + 1

def quickselect(A,p,r,k): # k - pozycja ktorej szukamy
    if p == r:
        return A[p]
    q = partition(A,p,r)
    if q == k:
        return A[q]
    if q < k:
        quickselect(A,q+1,r,k)
    else:
        quickselect(A,p,q-1,k)

"""def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)"""

arr  = [1,8,3,2,11,9,4]
# posortowana [1,2,3,4,8,9,11]
print(quickselect(arr,0,len(arr) - 1 , 3))




from random import randint as r
def counting_sort(A,n,limit): # A - array to sort , n - number of elements in array
    sorted = [0 for _ in range(n)]   # limit - biggest number in array
    count = [0 for _ in range(limit+1)]

    for i in range(n):
        count[A[i]] += 1

    for i in range(1,limit + 1):
        count[i] = count[i] + count[i-1]
    # 5 3 2 5 # 2(1) 3(2) 5(4)
    for i in range(n-1,-1,-1):
        count[A[i]] -= 1
        sorted[count[A[i]]] = A[i]
    for i in range(n):
        A[i] = sorted[i]

arr = [r(0,50) for i in range(20)]
print(arr)
counting_sort(arr,len(arr),max(arr))
print(arr)

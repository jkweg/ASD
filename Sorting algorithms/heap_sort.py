from math import floor
from random import randint as r

left = lambda i : 2*i + 1
right = lambda i : 2*i + 2
parent  = lambda i: floor((i-1)/2)

def heapify(A,n,i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind  = l
    if r < n and A[r] > A[max_ind]:
        max_ind  = r
    if max_ind != i:
        A[i],A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,i,0)
    return A

T = [r(-1999999,1999999) for i in range(200000000)]
#print(T)
T = heapsort(T)
print("Posortowane")

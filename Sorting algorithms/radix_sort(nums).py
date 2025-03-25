from random import randint as r

def counting_sort(T,k): # k - jakas potega 10 , zeby brac odpowiednia liczbe znaczaca
    C = [0]*len(T)
    B = [0] * 10
    for i in range(len(T)):
        idx = int((T[i]/k)%10)
        B[idx] += 1
    for i in range(1,10):
        B[i]+= B[i-1]
    for j in range(len(T)-1,-1,-1):
        idx = int((T[j]/k)%10)
        B[idx] -= 1
        C[B[idx]] = T[j]
    for i in range(len(T)):
        T[i] = C[i]

def radix_sort(T):
    maxi = 0
    for i in range(len(T)):
        maxi = max(maxi,T[i])
    i = 1
    while maxi/i > 0:
        counting_sort(T,i)
        i*=10


arr = [r(0,99) for _ in range(25)]
print(arr)
radix_sort(arr)
print(arr)
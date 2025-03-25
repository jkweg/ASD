import time
import random
from random import randint, shuffle


def insertion_sort(T):
    n = len(T)
    if n == 0 or n == 1:
        return T
    for i in range(1,n):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key


array = []
for j in range(2000000):
    array.append(j)
shuffle(array)
print("Timer start!")
start = time.time()
insertion_sort(array)
#print(array)
end = time.time()
print("Timer stopped")
print(end - start)

import time
import random
from random import randint, shuffle, randrange


def merge_sort(T):
    n = len(T)
    if n > 1:
        left_arr = T[:n//2]
        right_arr = T[n//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)
        #laczenie
        i = 0 # lewa strona
        j = 0 # prawa
        k = 0 # tablica wynikowa
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                T[k] = left_arr[i]
                i+=1
            else:
                T[k] = right_arr[j]
                j+=1
            k+=1
        while i < len(left_arr):
            T[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            T[k] =right_arr[j]
            j+=1
            k+=1
    return T

array = []
for j in range(2000000):
    array.append(j)
shuffle(array)
print("Timer start!")
start = time.time()
merge_sort(array)
#print(array)
end = time.time()
print("Timer stopped")
print(end - start)

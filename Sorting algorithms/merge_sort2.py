from random import randint as r

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    left_arr = merge_sort(arr[:n//2])
    right_arr = merge_sort(arr[n//2:])
    return merge(left_arr,right_arr)

def merge(a,b):
    i = j = k = 0
    merged = [0] * (len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            j += 1
        k+=1

    while i < len(a):
        merged[k] = a[i]
        k+=1
        i+=1
    while j < len(b):
        merged[k] = b[j]
        j+=1
        k+=1

    return merged


T = [r(-49,49) for i in range(20)]
print(T)
T = merge_sort(T)
print(T)
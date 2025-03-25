licznik = 0
def merge_sort(arr):
    global licznik
    n = len(arr)
    if n <= 1:
        return arr
    left_arr = merge_sort(arr[:n//2])
    right_arr = merge_sort(arr[n//2:])
    return merge(left_arr,right_arr)

def merge(a,b):
    global licznik
    i = j = k = 0
    merged = [0] * (len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            licznik += len(a) - i
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

def count_inv(arr):
    global licznik
    licznik = 0
    merge_sort(arr)
    return licznik

arr = [1,20,6,4,5,20,3,1]
print(count_inv(arr))
def counting_sort(T):  # sort 1 słowa
    n = len(T)
    if n < 2: return T
    B = [None] * n
    C = [0] * 26
    res = ''

    for i in range(n):
        C[ord(T[i]) - ord('a')] += 1

    for i in range(1, 26):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[ord(T[i]) - ord('a')] - 1] = T[i]
        C[ord(T[i]) - ord('a')] -= 1

    for letter in B:
        res += letter

    return res


arr = ["kot","pies","kaczka"]
for i in range(len(arr)):
    arr[i] = counting_sort(arr[i])
print(arr)
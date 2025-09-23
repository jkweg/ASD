# Agorytm ktory znaduje najduzszy rosnacy podciag , nie musi byc spojny

def LIS(T): #n^2
    n = len(T)
    dp = [1] * n
    maxi = 1
    best_end = 0
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if T[j] < T[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

        if dp[i] > maxi:
            maxi = dp[i]
            best_end = i
    
    seq = []

    i = best_end
    while i != -1:
        seq.append(T[i])
        i = prev[i]
    
    
    return maxi,seq[::-1]

def LIS2(T): # nlogn

    def lower_bound(a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    tails = []
    for x in T:
        i = lower_bound(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(LIS(nums))
print(LIS2(nums))

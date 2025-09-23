# Mamy ograniczona wage i chcemy jak najwieksza wartosc
# Kazdy przedmiot ma wage i wartosc

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # nie biorę przedmiotu i
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][W]

w = [2,3,4,5]
v  = [3,4,5,6]
Wm = 5
print(knapsack(w, v, Wm))

from egz2atesty import runtests


def wired(T):
    """
    T: lista długości m = 2n z parametrami mocy wejść
    Zwraca minimalny koszt bezprzecinającego się perfect matchingu.
    Złożoność: O(m^3), pamięć O(m^2).
    """
    m = len(T)
    INF = 10**18
    # dp[l][r] = minimalny koszt sparowania wszystkich punktów w [l..r]
    # (zakładamy, że r-l+1 jest parzyste)
    dp = [[0 if l > r else INF for r in range(m)] for l in range(m)]

    # rozważamy kolejne długości przedziałów (2, 4, 6, …, m)
    for length in range(2, m+1, 2):
        for l in range(0, m-length+1):
            r = l + length - 1
            best = INF
            # parujemy l z k, gdzie (k-l) jest nieparzyste
            for k in range(l+1, r+1, 2):
                cost_lk = 1 + abs(T[l] - T[k])
                left   = dp[l+1][k-1] if k-1 >= l+1 else 0
                right  = dp[k+1][r]   if k+1 <= r   else 0
                total  = left + right + cost_lk
                if total < best:
                    best = total
            dp[l][r] = best

    return dp[0][m-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )

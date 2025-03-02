import sys
input = sys.stdin.readline

def solution():
    n, s, m = map(int, input().split())
    v = [0] + list(map(int, input().split()))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][s] = 1
    
    for i in range(1, n + 1):
        for p in range(m + 1):
            if p + v[i] <= m:
                dp[i][p + v[i]] |= dp[i - 1][p]
            if p - v[i] >= 0:
                dp[i][p - v[i]] |= dp[i - 1][p]

    for i in range(m, -1, -1):
        if dp[n][i]:
            return i
    return -1
    
print(solution())
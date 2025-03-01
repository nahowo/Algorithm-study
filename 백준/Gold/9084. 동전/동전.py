import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (1 + m) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if coins[i] <= m:
            dp[i][coins[i]] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            v = coins[i]
            dp[i][j] += dp[i - 1][j]
            if j - v > 0:
                dp[i][j] += dp[i][j - v]
    
    return dp[n][m]

t = int(input())
for _ in range(t):
    print(solution())
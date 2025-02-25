import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]

print(solution())
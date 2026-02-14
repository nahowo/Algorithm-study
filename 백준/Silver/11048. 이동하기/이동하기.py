import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    candy = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = candy[0][0]
    for i in range(1, n):
        dp[i][0] = candy[i][0] + dp[i - 1][0]
    for j in range(1, m):
        dp[0][j] = candy[0][j] + dp[0][j - 1]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = candy[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[n - 1][m - 1]

print(solution())
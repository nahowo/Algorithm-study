import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    jump = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (n) for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if dp[i][j] and jump[i][j]:
                if i + jump[i][j] < n:
                    dp[i + jump[i][j]][j] += dp[i][j]
                if j + jump[i][j] < n:
                    dp[i][j + jump[i][j]] += dp[i][j]
    
    return dp[n - 1][n - 1]

print(solution())
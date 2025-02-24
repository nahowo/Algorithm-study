import sys
input = sys.stdin.readline
DIV = 10007

def solution():
    n = int(input())
    dp = [[0] * (10) for _ in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1
    
    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j, 10):
                dp[i][j] += (dp[i - 1][k]) % DIV
                dp[i][j] %= DIV

    return sum(dp[n]) % DIV

print(solution())
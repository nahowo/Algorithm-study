import sys
input = sys.stdin.readline
DIV = 9901

def solution():
    n = int(input())
    dp = [[0, 0, 0] for _ in range(n + 2)]
    dp[1] = [1, 1, 1]
    for i in range(2, n + 1):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % DIV
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % DIV
        dp[i][2] = (sum(dp[i - 1])) % DIV
    return sum(dp[n]) % DIV

print(solution())
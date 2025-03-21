import sys
input = sys.stdin.readline
DIV = 10

def solution():
    n = int(input())
    dp = [0] * (n + 2)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % DIV
    return dp[n - 1] % DIV
    
print(solution())
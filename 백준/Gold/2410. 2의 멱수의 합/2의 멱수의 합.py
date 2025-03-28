import sys
input = sys.stdin.readline
DIV = 10 ** 9

def solution():
    n = int(input())
    dp = [0] * (n + 2)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1]
        if i % 2 == 0:
            dp[i] += dp[i // 2]
        dp[i] %= DIV
    return dp[n]
    
print(solution())
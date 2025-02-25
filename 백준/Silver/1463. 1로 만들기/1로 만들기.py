import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 6

def solution():
    n = int(input())
    dp = [MAX_SIZE] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)
    return dp[n]

print(solution())
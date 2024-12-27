import sys
input = sys.stdin.readline
div = 1000000007

def solution():
    n = int(input())
    dp = [1] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] += (dp[i - 2] + dp[i - 1]) % div
    return dp[n]
    
print(solution())
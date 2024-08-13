import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [i for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, int(i ** (1 / 2)) + 1):
            dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)
    
    return dp[n]
    
print(solution())
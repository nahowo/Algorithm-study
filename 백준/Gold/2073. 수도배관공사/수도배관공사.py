import sys
input = sys.stdin.readline
MAX_SIZE = 2 ** 23 + 1

def solution():
    d, p = map(int, input().split())
    dp = [0] * (d + 1)
    dp[0] = MAX_SIZE

    for i in range(p):
        l, c = map(int, input().split())
        for j in range(d, l - 1, -1):
            dp[j] = max(dp[j], min(dp[j - l], c))    
    return dp[d]

print(solution())
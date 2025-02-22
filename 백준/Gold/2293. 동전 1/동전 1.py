import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]
    coin.sort()
    dp = [0] * (k + 1)
    dp[0] = 1
    for c in coin:
        for i in range(c, k + 1):
            dp[i] += dp[i - c]
    return dp[k]

print(solution())
import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 9

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0]
    sell = a[0]

    for i in range(1, n):
        sell = min(sell, a[i])
        dp[i] = max(dp[i - 1], a[i] - sell)

    return dp[n - 1]

print(solution())
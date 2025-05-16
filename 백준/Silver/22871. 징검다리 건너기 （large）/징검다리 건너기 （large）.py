import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 10

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [MAX_SIZE] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i + 1, n):
            k = max(dp[i], ((j - i) * (1 + abs(a[i] - a[j]))))
            dp[j] = min(dp[j], k)
    return dp[n - 1]

print(solution())
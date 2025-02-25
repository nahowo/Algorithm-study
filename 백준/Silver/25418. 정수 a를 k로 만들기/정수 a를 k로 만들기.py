import sys
input = sys.stdin.readline

def solution():
    a, k = map(int, input().split())
    dp = [k - a] * (k + 1)
    dp[a] = 0

    for i in range(a + 1, k + 1):
        if dp[i - 1] + 1 < dp[i]:
            dp[i] = dp[i - 1] + 1
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
    return dp[k]

print(solution())
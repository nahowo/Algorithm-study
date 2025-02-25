import sys
input = sys.stdin.readline

def solution():
    h, y = map(int, input().split())
    dp = [h] * (y + 1)

    for i in range(1, y + 1):
        if i - 1 >= 0:
            dp[i] = max(dp[i], int(dp[i - 1] * 105 / 100))
        if i - 3 >= 0:
            dp[i] = max(dp[i], int(dp[i - 3] * 120 / 100))
        if i - 5 >= 0:
            dp[i] = max(dp[i], int(dp[i - 5] * 135 / 100))

    return dp[y]

print(solution())
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    stair = [int(input()) for _ in range(n)] + [0, 0, 0]
    dp = [0] * (n + 3)
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], 
                    dp[i - 2] + stair[i])
    return dp[n - 1]

print(solution())
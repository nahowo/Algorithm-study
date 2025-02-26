import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    w = [0] + [int(input()) for _ in range(n)] + [0]
    dp = [0] * (n + 2)
    dp[1], dp[2] = w[1], w[1] + w[2]

    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1], # ? ? X
            dp[i - 2] + w[i], # O X O
            dp[i - 3] + w[i - 1] + w[i] # X O O
        )

    return dp[n]

print(solution())
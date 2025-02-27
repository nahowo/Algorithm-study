import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    counsel = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 2)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i], dp[i - 1])
        if i + counsel[i - 1][0] <= n + 1:
            dp[i + counsel[i - 1][0]] = max(dp[i + counsel[i - 1][0]], dp[i] + counsel[i - 1][1])
    dp[n + 1] = max(dp[n + 1], dp[n])
    return dp[n + 1]

print(solution())
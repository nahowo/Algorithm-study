import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    m = int(input())
    seat = [0] * (n + 2)
    for _ in range(m):
        seat[int(input())] = 1
    dp = [0] * (n + 2)
    dp[1] = 1
    if seat[2] != 1 and seat[1] != 1:
        dp[2] = 2
    else:
        dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1]
        if seat[i] != 1 and seat[i - 1] != 1:
            dp[i] += dp[i - 2]

    return dp[n]

print(solution())
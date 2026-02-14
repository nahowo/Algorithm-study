import sys
input = sys.stdin.readline

def solution():
    global dp
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 1, 1

    for i in range(2, 12):
        dp[i] += dp[i - 1]
        if i > 2:
            dp[i] += dp[i - 2]
        if i > 3:
            dp[i] += dp[i - 3]

solution()
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
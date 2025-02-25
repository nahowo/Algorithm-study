import sys
input = sys.stdin.readline

def solution():
    winner = ["CY", "SK"] # dp[i] == 0이면 상근이 패배, 1이면 상근이 승리
    n = int(input())
    dp = [0] * (n + 3)
    dp[2] = 1

    for i in range(4, n + 1):
        dp[i] = int(dp[i - 1] & dp[i - 3] == 0)

    return winner[dp[n]]

print(solution())
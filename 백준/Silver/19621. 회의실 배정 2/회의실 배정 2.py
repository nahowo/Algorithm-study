import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    meeting = []
    for _ in range(n):
        meeting.append(list(map(int, input().split())))
    if n == 1:
        return meeting[0][2]
    meeting.sort(key = lambda x: x[0])
    dp = [0] * n
    dp[0] = meeting[0][2]
    dp[1] = max(meeting[0][2], meeting[1][2])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + meeting[i][2])

    return dp[n - 1]

print(solution())
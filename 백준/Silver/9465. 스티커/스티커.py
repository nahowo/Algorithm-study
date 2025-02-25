import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    score = []
    for _ in range(2):
        score.append(list(map(int, input().split())))
    dp = [[0, 0] for _ in range(n)]
    dp[0][0], dp[0][1] = score[0][0], score[1][0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1] + score[0][i], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][0] + score[1][i], dp[i - 1][1])
    return max(dp[n - 1])

t = int(input())
for _ in range(t):
    print(solution())
import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 9

def solution():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for s in range(0, n - i): # 시작 위치
            dp[s][s + i] = MAX_SIZE
            for t in range(s, s + i):
                dp[s][s + i] = min(dp[s][s + i], dp[s][t] + dp[t + 1][s + i] + (matrix[s][0] * matrix[t][1] * matrix[s + i][1]))
    return dp[0][n - 1]

print(solution())
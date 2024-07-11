import sys
input = sys.stdin.readline

def solution():
    n, m = map(int,input().split())
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    chapters = [[0, 0]]
    for _ in range(m):
        chapters.append(list(map(int,input().split())))
    chapters.sort()
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j < chapters[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - chapters[i][0]] + chapters[i][1])

    return dp[m][n]

print(solution())
import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 6

def solution():
    n = int(input())
    colors = []
    for _ in range(n):
        colors.append(list(map(int, input().split())))
    rgbMin = [MAX_SIZE] * 3

    for c in range(3): # R, G, B
        dp = [[MAX_SIZE] * 3 for _ in range(n)]
        dp[0][c] = colors[0][c]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + colors[i][j]
        dp[n - 1][c] = MAX_SIZE
        rgbMin[c] = min(dp[n - 1])
    
    return min(rgbMin)

print(solution())
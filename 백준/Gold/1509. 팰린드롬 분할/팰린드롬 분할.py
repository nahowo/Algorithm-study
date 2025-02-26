import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    n = len(s)
    isP = [[0] * n for _ in range(n)]

    for start in range(n):
        isP[start][start] = 1
    for end in range(1, n):
        start = end - 1
        if s[start] == s[end]:
            isP[start][end] = 1
    for end in range(2, n): # 종료점
        for start in range(end - 1): # 시작점
            if s[start] == s[end] and isP[start + 1][end - 1]:
                isP[start][end] = 1

    dp = [i for i in range(n + 1)]
    for end in range(1, n + 1): # 종료점
        for start in range(end + 1): # 시작점
            if isP[start - 1][end - 1]:
                dp[end] = min(dp[end], dp[start - 1] + 1)

    return dp[n]

print(solution())
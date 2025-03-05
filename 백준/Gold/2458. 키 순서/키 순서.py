import sys
input = sys.stdin.readline
INF = 10 ** 8

def solution():
    n, m = map(int, input().split())
    height = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        height[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if height[i][k] and height[k][j]:
                    height[i][j] = 1
    
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if height[i][j] or height[j][i]:
                cnt[i] += 1
    answer = 0
    for i in range(1, n + 1):
        if cnt[i] == n - 1:
            answer += 1
    return answer

print(solution())
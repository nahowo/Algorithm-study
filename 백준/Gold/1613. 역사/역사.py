import sys
from collections import deque
input = sys.stdin.readline
INF = 10 ** 4

def solution():
    n, k = map(int, input().split())
    order = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        order[a].append(b)

    answer = [[0] * (n + 1) for _ in range(n + 1)]
    for sx in range(1, n + 1):
        q = deque([sx])
        visited = [False] * (n + 1)
        visited[sx] = True
        while q:
            x = q.popleft()
            for nx in order[x]:
                if not visited[nx]:
                    visited[nx] = True
                    answer[sx][nx] = -1
                    answer[nx][sx] = 1
                    q.append(nx)

    s = int(input())
    for _ in range(s):
        a, b = map(int, input().split())
        print(answer[a][b])

solution()
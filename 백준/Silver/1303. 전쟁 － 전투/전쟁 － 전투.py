import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(visited, target, sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = True
    power = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == target and not visited[nx][ny]:
                visited[nx][ny] = True
                power += 1
                q.append([nx, ny])
    return power ** 2

def solution():
    global maps, n, m
    n, m = map(int, input().split())
    maps = [input().rstrip() for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    power = {"W": 0, "B": 0}

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                power[maps[i][j]] += bfs(visited, maps[i][j], i, j)
    print(power['W'], power['B'])

solution()
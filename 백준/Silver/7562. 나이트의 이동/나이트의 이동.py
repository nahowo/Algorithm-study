import sys
from collections import deque
input = sys.stdin.readline
d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

def bfs(l, sx, sy, ex, ey):
    cnt = [[-1] * l for _ in range(l)]
    cnt[sx][sy] = 0
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return cnt[x][y]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and cnt[nx][ny] == -1:
                cnt[nx][ny] = cnt[x][y] + 1
                q.append([nx, ny])

def solution():
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    return bfs(l, sx, sy, ex, ey)

t = int(input())
for _ in range(t):
    print(solution())
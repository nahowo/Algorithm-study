import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    m, n = map(int, input().split())
    maps = [input().rstrip() for _ in range(n)]
    visited = [[-1] * (m) for _ in range(n)]
    visited[0][0] = 0
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            break
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if maps[nx][ny] == '0':
                    q.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return visited[n - 1][m - 1]

print(solution())
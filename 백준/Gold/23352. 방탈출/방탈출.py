import sys
from collections import deque
input = sys.stdin.readline
D = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(sx, sy):
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1
    tmplen = 1
    tmpDestX = sx
    tmpDestY = sy
    q = deque()
    q.append([sx, sy])

    while q:
        x, y = q.popleft()
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if MAP[nx][ny] != 0 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] > tmplen:
                        tmplen = visited[nx][ny]
                        tmpDestX = nx
                        tmpDestY = ny
    
    return tmplen, tmpDestX, tmpDestY

def solution():
    global MAP, n, m
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    length = 0

    for i in range(n):
        for j in range(m):
            if MAP[i][j]:
                l, x, y = bfs(i, j)
                if l > length:
                    length = l
                    answer = MAP[i][j] + MAP[x][y]
                elif l == length:
                    length = l
                    answer = max(answer, MAP[i][j] + MAP[x][y])
                        
    return answer

print(solution())
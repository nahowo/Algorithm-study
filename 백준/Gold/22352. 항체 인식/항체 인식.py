import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1) ,(0, -1), (1, 0), (-1, 0)]

def solution():
    n, m = map(int, input().split())
    pre = [list(map(int, input().split())) for _ in range(n)]
    post = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    changed = 0

    for sx in range(n):
        for sy in range(m):
            if not visited[sx][sy]:
                q = deque()
                q.append([sx, sy])
                visited[sx][sy] = True
                changedTo = post[sx][sy]
                if pre[sx][sy] != post[sx][sy]:
                    changed += 1
                tmpV = [[False] * m for _ in range(n)]
                tmpV[sx][sy] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not tmpV[nx][ny]:
                            if pre[x][y] == pre[nx][ny]:
                                if post[nx][ny] != changedTo:
                                    changed += 1
                                    break
                                else:
                                    tmpV[nx][ny] = True
                                    visited[nx][ny] = True
                                    q.append([nx, ny])
                
    if changed > 1:
        return "NO"
    return "YES"

print(solution())
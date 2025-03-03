import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    n, m = map(int, input().split())
    maps = [input().rstrip() for _ in range(n)]
    cnt = [[[0, 0] for _ in range(m)] for _ in range(n)]
    cnt[0][0][0] = 1
    q = deque()
    q.append([0, 0, 0])
    
    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt[x][y][c]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == '0' and cnt[nx][ny][c] == 0:
                    cnt[nx][ny][c] = cnt[x][y][c] + 1
                    q.append([nx, ny, c])
                elif maps[nx][ny] == '1' and c == 0 and cnt[nx][ny][1] == 0:
                    cnt[nx][ny][1] = cnt[x][y][c] + 1
                    q.append([nx, ny, 1])

    return -1

print(solution())
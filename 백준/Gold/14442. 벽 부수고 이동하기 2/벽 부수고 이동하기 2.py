import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    n, m, k = map(int, input().split())
    maps = [input().rstrip() for _ in range(n)]
    cnt = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
    cnt[0][0][0] = 1
    q = deque()
    q.append([0, 0, 0]) # x, y, 벽 파괴 여부
    
    while q:
        x, y, flag = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt[x][y][flag]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == '0' and cnt[nx][ny][flag] == -1:
                    cnt[nx][ny][flag] = cnt[x][y][flag] + 1
                    q.append([nx, ny, flag])
                elif maps[nx][ny] == '1' and flag < k and cnt[nx][ny][flag + 1] == -1:
                    cnt[nx][ny][flag + 1] = cnt[x][y][flag] + 1
                    q.append([nx, ny, flag + 1])
    return -1
    
print(solution())
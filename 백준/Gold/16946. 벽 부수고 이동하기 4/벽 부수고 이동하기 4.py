import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(sx, sy):
    global idx
    q = deque()
    q.append([sx, sy])
    basic[sx][sy] = '1'
    wallCnt[sx][sy] = idx
    wall[idx] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and basic[nx][ny] == '0':
                basic[nx][ny] = '1'
                wallCnt[nx][ny] = idx
                wall[idx] += 1
                q.append([nx, ny])
    idx += 1
    return

def solution():
    global wall, basic, n, m, wallCnt, idx
    n, m = map(int, input().split())
    wall = dict()
    basic = []
    for _ in range(n):
        basic.append(list(input().rstrip()))
    wallCnt = [[False] * (m) for _ in range(n)]
    movable = [['0'] * (m) for _ in range(n)]

    idx = 1
    for i in range(n):
        for j in range(m):
            if basic[i][j] == '0':
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if wallCnt[i][j] == False:
                tmpS = set()
                cnt = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and wallCnt[ni][nj] != False:
                        if wallCnt[ni][nj] not in tmpS:
                            tmpS.add(wallCnt[ni][nj])
                            cnt += wall[wallCnt[ni][nj]] # 이동 가능 방
                movable[i][j] = str((cnt + 1) % 10)
    
    for i in movable:
        print(''.join(i))

solution()
import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   
def setCnt():
    return [[-1] * n for _ in range(m)]

def bfs(sx, sy, ex, ey):
    cnt = setCnt()
    cnt[sx][sy] = 0
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return cnt[x][y]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and cnt[nx][ny] == -1 and room[nx][ny] != '#':
                cnt[nx][ny] = cnt[x][y] + 1
                q.append([nx, ny])

def calcDist(route, sx, sy, ex, ey):
    coordinate = [[sx, sy]]
    for i in range(len(pos)):
        coordinate.append([pos[route[i]][0], pos[route[i]][1]])
    coordinate.append([ex, ey])

    dist = 0
    for i in range(len(coordinate) - 1):
        dist += bfs(coordinate[i][0], coordinate[i][1], coordinate[i + 1][0], coordinate[i + 1][1])
    return dist

def solution():
    global room, n, m, pos
    n, m = map(int, input().split())
    room = [list(input().rstrip()) for _ in range(m)]
    dist = 10 ** 8

    pos = []
    for i in range(m):
        for j in range(n):
            if room[i][j] == 'X':
                pos.append([i, j])
            elif room[i][j] == 'S':
                sx, sy = i, j
            elif room[i][j] == 'E':
                ex, ey = i, j
    
    perm = list(permutations(range(len(pos)), len(pos)))
    for i in range(len(perm)):
        dist = min(dist, calcDist(perm[i], sx, sy, ex, ey))
    return dist
    
print(solution())
import sys
from collections import deque
input = sys.stdin.readline
direction = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
switch = lambda x: 0 if x else 1
MAX_SIZE = 0

def solution():
    n = int(input())
    home = [input().rstrip() for _ in range(n)]
    cnt = [[MAX_SIZE] * n for _ in range(n)]
    si, sj, ei, ej = findDoor(home, n)
    cnt[si][sj] = 0
    q = deque()
    q.append([si, sj, 0])
    q.append([si, sj, 1])

    while q:
        x, y, d = q.popleft()
        for dx, dy in direction[d]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n:
                if home[nx][ny] == '*':
                    break
                elif home[nx][ny] == '!' and cnt[nx][ny] == MAX_SIZE:
                    q.append([nx, ny, switch(d)])
                    cnt[nx][ny] = cnt[x][y] + 1
                elif nx == ei and ny == ej:
                    return cnt[x][y]
                nx += dx
                ny += dy

def findDoor(home, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if home[i][j] == '#':
                count += 1
                if count == 1:
                    si, sj = i, j
                if count == 2:
                    return si, sj, i, j

print(solution())
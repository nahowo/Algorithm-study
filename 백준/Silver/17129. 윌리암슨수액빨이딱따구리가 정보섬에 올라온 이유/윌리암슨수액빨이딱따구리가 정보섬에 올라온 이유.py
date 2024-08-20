import sys
from collections import deque
input = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(sx, sy):
    q = deque([])
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if 3 <= island[nx][ny] <= 5:
                    return (-1) * (island[x][y]) + 1

                if island[nx][ny] == 0:
                    q.append([nx, ny])
                    island[nx][ny] = island[x][y] - 1
    return False

def solution():
    global island, n, m
    n, m = map(int, input().split())
    island = []
    for i in range(n):
        tmp = list(map(int, input().rstrip()))
        if 2 in tmp:
            x = i
            y = tmp.index(2)
            tmp[y] = 0
        island.append(tmp)
    
    result = bfs(x, y)
    if result != False:
        print("TAK")
        print(result)
    else:
        print("NIE")

solution()
import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def move(q, swanPos, visited, lake):
    nq = deque()
    while q:
        x, y = q.popleft()
        if x == swanPos[1][0] and y == swanPos[1][1]:
            return True, []
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if lake[nx][ny] == 'X':
                    nq.append([nx, ny])
                else:
                    q.append([nx, ny])
                visited[nx][ny] = True
    return False, nq

def melt(q, lake):
    nq = deque()
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if lake[nx][ny] == 'X':
                    nq.append([nx, ny])
                    lake[nx][ny] = '.'
    return nq

def solution():
    global r, c
    r, c = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(r)]
    day = 0
    waterQ = deque()
    swanPos = [0] * 2
    swanCnt = 0
    swanQ = deque()
    visited = [[False] * c for _ in range(r)] # 백조 방문 여부

    for i in range(r):
        for j in range(c):
            if lake[i][j] == '.' or lake[i][j] == 'L':
                if lake[i][j] == 'L':
                    swanPos[swanCnt] = ([i, j])
                    swanCnt += 1
                    if swanCnt == 1:
                        visited[i][j] = True
                        swanQ.append([i, j])
                waterQ.append([i, j])
                
    while True:
        canMeet, swanQ = move(swanQ, swanPos, visited, lake)
        if canMeet:
            return day
        waterQ = melt(waterQ, lake)
        day += 1

print(solution())
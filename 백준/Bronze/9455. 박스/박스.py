import sys
input = sys.stdin.readline

def calcDest(): # 도착해야 할 위치를 구하는 함수
    for j in range(n):
        boxCnt = 0
        for i in range(m - 1, -1, -1):
            if grid[i][j] == 1:
                dest[i][j] = boxCnt
                boxCnt += 1
    return

def calcDist(j): # 이동거리를 구하는 함수
    dist = 0
    for i in range(m):
        if grid[i][j] == 1:
            dist += (m - i - 1) - dest[i][j]
    return dist

def solution():
    global m, n, grid, dest, pos
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    
    dest = [[0] * (n) for _ in range(m)] # 도착해야 할 위치(y축)
    calcDest()

    totalDist = 0
    for j in range(n):
        totalDist += calcDist(j)
    return totalDist

t = int(input())
for _ in range(t):
    print(solution())
import sys
from collections import deque
import heapq
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 5

def calcDist(maps): # dist[sx][sy][ex][ey] = sx, sy -> ex, ey까지의 최단거리
    dist = [[[[-1] * (n) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for sx in range(n):
        for sy in range(n):
            if maps[sx][sy] != 1:
                visited = [[False] * n for _ in range(n)]
                visited[sx][sy] = True
                dist[sx][sy][sx][sy] = 0
                q = deque()
                q.append([sx, sy])
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            dist[sx][sy][nx][ny] = dist[sx][sy][x][y] + 1
                            q.append([nx, ny])
    return dist

def nextPos(sx, sy, pos, dist):
    dists = []
    for i, p in pos.items():
        px, py = p[0], p[1]
        heapq.heappush(dists, [dist[sx][sy][px][py], px, py, i])
    minDist = dists[0]
    return minDist[0], minDist[3] # 거리, 손님 인덱스

def solution():
    global n, m
    n, m, fuel = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    pos = dict()
    for i in range(m):
        tmp = list(map(int, input().split()))
        pos[i] = [tmp[0] - 1, tmp[1] - 1, tmp[2] - 1, tmp[3] - 1]
    dist = calcDist(maps)
    for x1, y1, x2, y2 in pos.values():
        if dist[x1][y1][x2][y2] == -1 or dist[sx][sy][x1][y1] == -1:
            return -1

    # 가까운 손님부터 이동
    while fuel and len(pos) > 0:
        tmpDist1, tmpI = nextPos(sx, sy, pos, dist)
        # 손님까지 운전
        fuel -= tmpDist1
        if fuel < 0:
            return -1
        sx, sy = pos[tmpI][0], pos[tmpI][1]
        nx, ny = pos[tmpI][2], pos[tmpI][3]
        # 손님에서 도착지
        tmpDist2 = dist[sx][sy][nx][ny]
        if fuel - tmpDist2 < 0:
            return -1
        sx, sy = nx, ny
        fuel += tmpDist2
        # 손님 삭제
        del pos[tmpI]
    return fuel
    
print(solution())
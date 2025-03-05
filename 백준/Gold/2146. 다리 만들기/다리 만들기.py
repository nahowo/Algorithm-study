import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 4

def getIsland():
    idx = 1
    visited = [[False] * n for _ in range(n)]
    edge = dict()

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maps[i][j] == 1:
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                maps[i][j] = idx
                edge[idx] = set()
                while q:
                    x, y = q.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            if maps[nx][ny] == 1:
                                q.append([nx, ny])
                                maps[nx][ny] = idx
                            else:
                                edge[idx].add((x, y))
                idx += 1
    return edge

def getMinBridge(idx, coordinate):
    tmpMinDist = INF
    for sx, sy in coordinate:
        q = deque()
        q.append([sx, sy])
        dist = [[-1] * n for _ in range(n)]
        dist[sx][sy] = 0
        while q:
            x, y = q.popleft()
            if maps[x][y] != idx and maps[x][y] > 0:
                tmpMinDist = min(tmpMinDist, dist[x][y] - 1)
                break
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != idx and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
    return tmpMinDist

def solution():
    global n, maps
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    # 섬을 인덱스로 구분하고 가장자리 좌표 구하기
    edge = getIsland()

    # 각 가장자리 좌표에서 다른 섬으로 가는 최단거리 구하기
    answer = INF

    for idx, coordinate in edge.items():
        tmpMinBridge = getMinBridge(idx, coordinate)
        answer = min(answer, tmpMinBridge)
    return answer

print(solution())
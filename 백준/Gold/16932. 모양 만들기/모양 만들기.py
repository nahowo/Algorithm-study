import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(n, m):
    idx = 2
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                ocean.append([i, j])
            if not visited[i][j] and maps[i][j] == 1:
                visited[i][j] = True
                maps[i][j] = idx
                cnt = 1
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            cnt += 1
                            maps[nx][ny] = idx
                            q.append([nx, ny])
                island[idx] = cnt
                idx += 1

def solution():
    global island, ocean, maps
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    island = dict()
    ocean = []
    bfs(n, m)
    answer = 1

    for x, y in ocean:
        tmpCnt = 1
        checked = set()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and maps[nx][ny] not in checked:
                checked.add(maps[nx][ny])
                tmpCnt += island[maps[nx][ny]]
        answer = max(answer, tmpCnt)

    return answer
    
print(solution())
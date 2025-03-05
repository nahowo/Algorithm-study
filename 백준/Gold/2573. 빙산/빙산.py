import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 7 + 1

def findInit():
    q = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0:
                q.append([i, j])
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            if maps[nx][ny] > 0:
                                q.append([nx, ny])
                                cnt += 1
                            visited[nx][ny] = True
                return i, j, cnt
    return 0, 0, 0

def melt(sx, sy, iceCnt):
    global maps
    q = deque([])
    q.append([sx, sy])
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    cnt = 0
    nxtMelt = 0
    nxtMaps = deepcopy(maps)
    nsx, nsy = sx, sy # 다음 시작 위치

    while q:
        x, y = q.popleft()
        dgr = 0
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

                if maps[nx][ny] == 0:
                        dgr += 1
        if maps[x][y] - dgr <= 0:
            nxtMelt += 1
        else:
            nsx, nsy = x, y
            cnt += 1
        nxtMaps[x][y] = max(0, maps[x][y] - dgr)

    maps = deepcopy(nxtMaps)
    if iceCnt - nxtMelt > cnt:
        return False, cnt, nsx, nsy
    return True, cnt, nsx, nsy

def solution():
    # 주변의 0 개수만큼 줄어들음
    # 사라지는 빙산은 현재 숫자 - 현재 주변 0 개수
    # 사라지는 빙산의 개수를 세기 -> 다음 단계에서 count가 기존값 - 사라지는 빙산보다 작다면 갈라짐
    global n, m, maps
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    sx, sy, cnt = findInit()

    iceCnt = cnt

    for year in range(iceCnt):
        flag, nxtCnt, nsx, nsy = melt(sx, sy, cnt)
        if not flag:
            return year
        if nxtCnt == 0:
            break
        cnt = nxtCnt
        sx, sy = nsx, nsy

    return 0

print(solution())
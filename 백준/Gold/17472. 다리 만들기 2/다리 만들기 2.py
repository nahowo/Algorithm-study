import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
vertical = [(1, 0), (-1, 0)]
horizontal = [(0, 1), (0, -1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def bfs(sx, sy, idx):
    q = deque()
    q.append([sx, sy])
    island[sx][sy] = idx
    cdn = deque()
    cdn.append([sx, sy])

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and island[nx][ny] == -1:
                island[nx][ny] = idx
                cdn.append([nx, ny])
                q.append([nx, ny])
    return cdn

def findLength(i, q, direction):
    cnt = [[-1] * m for _ in range(n)]
    for sx, sy in q:
        cnt[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and cnt[nx][ny] == -1:
                j = island[nx][ny]
                if j == -1:
                    q.append([nx, ny])
                elif j != i and cnt[x][y] > 1:
                    dist[i][j] = min(dist[i][j], cnt[x][y]) # i섬~j섬 거리 업데이트
                cnt[nx][ny] = cnt[x][y] + 1

def solution():
    global n, m, dist, maps, island, parent
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    island = [[-1] * m for _ in range(n)]
    idx = 0
    coordinates = []

    # 섬 구분하기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and island[i][j] == -1:
                coordinates.append(bfs(i, j, idx))
                idx += 1
    
    # 섬끼리 최단거리 구하기
    dist = [[11] * idx for _ in range(idx)]
    for i in range(idx):
        findLength(i, coordinates[i].copy(), vertical)
        findLength(i, coordinates[i].copy(), horizontal)

    route = []
    graph = [[] for _ in range(idx)]
    for i in range(idx):
        for j in range(i + 1, idx):
            if dist[i][j] < 11:
                graph[i].append(j)
                graph[j].append(i)
                route.append([dist[i][j], i, j])
    route.sort()

    # 모든 섬을 연결할 수 있는지 확인
    visited = [False] * idx
    if route:
        q = deque()
        q.append(route[0][1])
        q.append(route[0][2])
        visited[route[0][1]] = True
        visited[route[0][2]] = True
        while q:
            x = q.popleft()
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
    if False in visited:
        return -1

    # MST
    answer = 0
    parent = [i for i in range(idx)]
    for l, a, b in route:
        if find(a) != find(b):
            answer += l
            union(a, b)

    return answer

print(solution())
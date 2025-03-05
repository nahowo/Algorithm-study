import sys, heapq
input = sys.stdin.readline
INF = 10 ** 12
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def findE(maps, h, w):
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'E':
                return i, j

def solution():
    k, w, h = map(int, input().split())
    ks = {'E': 0}
    for _ in range(k):
        a, b = input().rstrip().split()
        ks[a] = int(b)
    maps = [input().rstrip() for _ in range(h)]
    sx, sy = findE(maps, h, w)
    dist = [[INF] * w for _ in range(h)]
    dist[sx][sy] = 0
    q = [[0, sx, sy]]
    
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            return dist[x][y]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if dist[nx][ny] > d + ks[maps[nx][ny]]:
                    dist[nx][ny] = d + ks[maps[nx][ny]]
                    heapq.heappush(q, [dist[nx][ny], nx, ny])

t = int(input())
for _ in range(t):
    print(solution())
import sys, heapq
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 5

def solution():
    n, m= map(int, input().split())
    forest = [input().rstrip() for _ in range(n)]
    garbage = [[0] * m for _ in range(n)]
    around = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if forest[i][j] == 'S':
                sx, sy = i, j
            elif forest[i][j] == 'F':
                fx, fy = i, j
            elif forest[i][j] == 'g':
                garbage[i][j] = 1
            else:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and forest[ni][nj] == 'g':
                        around[i][j] = 1
                        break
    
    dist = [[[INF, INF] for _ in range(m)] for _ in range(n)] # 쓰레기, 쓰레기 옆
    dist[sx][sy] = [0, 0]
    q = [[0, 0, sx, sy]]
    while q:
        g, ga, x, y = heapq.heappop(q)
        if x == fx and y == fy:
            return g, ga
        if dist[x][y][0] < g:
            continue
        elif dist[x][y][0] == g and dist[x][y][1] < ga:
            continue
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                tg = g + garbage[nx][ny]
                tga = ga + around[nx][ny]
                if dist[nx][ny][0] > tg or (dist[nx][ny][0] == tg and dist[nx][ny][1] > tga):
                    dist[nx][ny][0] = tg
                    dist[nx][ny][1] = tga
                    heapq.heappush(q, [tg, tga, nx, ny])

    return dist[fx][fy][0], dist[fx][fy][1]

print(*solution())
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if cache[x][y] != -1:
        return cache[x][y]
    
    ret = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] > maps[x][y]:
            ret += dfs(nx, ny)
    cache[x][y] = ret
    return ret

def solution():
    global cache, n, m, maps
    m, n = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(m)]
    cache = [[-1] * n for _ in range(m)]
    return dfs(m - 1, n - 1)
    
print(solution())
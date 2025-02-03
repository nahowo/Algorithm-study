D = [(1, 0), (0, 1)]
DIV = 1000000007

def route(i, j, m, n, grid):
    if i == n - 1 and j == m - 1:
        return 1
    
    if cache[i][j] != -1:
        return cache[i][j]
    
    ret = 0
    for di, dj in D:
        ni, nj = i + di, j + dj
        if ni < n and nj < m and grid[ni][nj]:
            ret += (route(ni, nj, m, n, grid) % DIV) % DIV
    cache[i][j] = ret % DIV
    return cache[i][j]

def solution(m, n, puddles):
    global cache
    grid = [[True] * (m) for _ in range(n)]
    cache = [[-1] * (m) for _ in range(n)]
    for j, i in puddles:
        grid[i - 1][j - 1] = False
    
    answer = route(0, 0, m, n, grid)
    return answer
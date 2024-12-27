import sys
sys.setrecursionlimit(500 ** 2 + 1)
input = sys.stdin.readline
d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

escape = lambda x, y: True if (x < 0 or x >= n) or ((y < 0 or y >= m)) else False

def dfs(x, y):
    if escape(x, y):
        return 1
    if possible[x][y] != -1:
        return possible[x][y]

    possible[x][y] = 0
    dx, dy = d[maze[x][y]]
    nx, ny = x + dx, y + dy
    answer = dfs(nx, ny)
    possible[x][y] = answer
    return answer

def solution():
    global n, m, possible, maze
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(input().rstrip())
    possible = [[-1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if possible[i][j] != 1:
                dfs(i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if possible[i][j] == 1:
                cnt += 1
    return cnt

print(solution())
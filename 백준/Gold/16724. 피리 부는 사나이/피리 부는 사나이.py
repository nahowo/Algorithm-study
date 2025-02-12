import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 8
d = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

def dfs(x, y, idx):
    global answer
    if visited[x][y] != -1:
        if visited[x][y] == idx:
            answer += 1
        return
    visited[x][y] = idx
    nx, ny = x + d[board[x][y]][0], y + d[board[x][y]][1]
    dfs(nx, ny, idx)

def solution():
    global visited, board, answer
    answer = 0
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    
    idx = 0
    for i in range(n):
        for j in range(m):
            dfs(i, j, idx)
            idx += 1
    return answer

print(solution())
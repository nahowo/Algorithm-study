import sys
input = sys.stdin.readline

def dfs(k, cnt, color):
    global answer
    if answer[color] >= (cnt + l - k // 2):
        return
    if k >= l:
        answer[color] = max(answer[color], cnt)
        return
    
    for nx, ny in nxt[k]:
        if not visited[nx - ny]:
            visited[nx - ny] = 1
            dfs(k + 2, cnt + 1, color)
            visited[nx - ny] = 0
    dfs(k + 2, cnt, color)

def solution():
    global n, board, answer, l, nxt, visited
    answer = [0, 0]
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    l = 2 * n - 1
    nxt = [[] for _ in range(l)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                nxt[i + j].append((i, j))
    visited = [0] * l
    dfs(0, 0, 0)
    dfs(1, 0, 1)
    return sum(answer)
    
print(solution())
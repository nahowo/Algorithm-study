import sys, copy
input = sys.stdin.readline

def check():
    for i in range(3):
        tmp = 0
        for j in range(3):
            tmp += board[i][j]
        if tmp != 15:
            return False
        tmp = 0
        for j in range(3):
            tmp += board[j][i]
        if tmp != 15:
            return False
    if board[0][0] + board[1][1] + board[2][2] != 15:
        return False
    if board[0][2] + board[1][1] + board[2][0] != 15:
        return False
    return True

def addDist():
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs(board[i][j] - a[i][j])
    return result

def dfs(cnt):
    global minCnt
    if cnt == 9 and check():
        minCnt = min(minCnt, addDist())
        return
    
    x = cnt // 3
    y  = cnt % 3
    for i in range(1, 10):
        if not visited[i]:
            tmp = board[x][y]
            visited[i] = True
            board[x][y] = i
            dfs(cnt + 1)
            visited[i] = False
            board[x][y] = tmp

def solution():
    global board, a, minCnt, visited
    a = [list(map(int, input().split())) for _ in range(3)]
    board = copy.deepcopy(a)
    minCnt = 81
    visited = [False] * 10

    dfs(0)
    return minCnt
    
print(solution())
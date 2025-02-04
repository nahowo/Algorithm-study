import sys
input = sys.stdin.readline
dq = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
dk = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

def solution():
    n, m = map(int, input().split())
    board = [[0] * (m) for _ in range(n)]
    tmp = list(map(int, input().split()))
    q = tmp[0]
    queen = []
    for i in range(1, q * 2, 2):
        queen.append([tmp[i] - 1, tmp[i + 1] - 1])
        board[queen[-1][0]][queen[-1][1]] = 1
    tmp = list(map(int, input().split()))
    k = tmp[0]
    knight = []
    for i in range(1, k * 2, 2):
        knight.append([tmp[i] - 1, tmp[i + 1] - 1])
        board[knight[-1][0]][knight[-1][1]] = 2
    tmp = list(map(int, input().split()))
    p = tmp[0]
    pawn = []
    for i in range(1, p * 2, 2):
        pawn.append([tmp[i] - 1, tmp[i + 1] - 1])
        board[pawn[-1][0]][pawn[-1][1]] = 3
    
    # move queen
    for i, j in queen:
        for di, dj in dq:
            ni, nj = i + di, j + dj
            while 0 <= ni < n and 0 <= nj < m and (board[ni][nj] == 0 or board[ni][nj] == -1):
                board[ni][nj] = -1
                ni += di
                nj += dj
    
    # move knight
    for i, j in knight:
        for di, dj in dk:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and (board[ni][nj] == 0 or board[ni][nj] == -1):
                board[ni][nj] = -1
    
    # count
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1

    return cnt

print(solution())
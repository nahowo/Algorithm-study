import sys
from copy import deepcopy
input = sys.stdin.readline

def moveVertical(board, s, step):
    #  위: board, 0, 1
    # 아래: board, n - 1, -1
    global maxBlock
    # 0. 밀기
    if step == 1:
        start, end = 0, n
    else:
        start, end = n - 1, -1

    for j in range(n):
        q = [0] * n
        k = s
        for i in range(start, end, step):
            if board[i][j] != 0:
                q[k] = board[i][j]
                k += step
        for i in range(n):
            board[i][j] = q[i]

    # 1. 블록 합치기
    for j in range(n):
        i = s
        while (step == -1 and i > 0) or (step == 1 and i < n - 1):
            if board[i][j] == 0: # 현재 위치가 비어있을 때
                i += step
            else: # 현재 위치가 비어있지 않을 때
                if board[i][j] != board[i + step][j]: # 앞 블럭과 다른 블럭인 경우
                    i += step
                else: # 앞 블럭과 같은 블럭인 경우
                    board[i][j], board[i + step][j] = 0, board[i + step][j] * 2
                    maxBlock = max(maxBlock, board[i + step][j])
                    i += step * 2

    # 2. 빈 공간 지우기
    if step == 1:
        start, end = 0, n
    else:
        start, end = n - 1, -1

    for j in range(n):
        q = [0] * n
        k = s
        for i in range(start, end, step):
            if board[i][j] != 0:
                q[k] = board[i][j]
                k += step
        for i in range(n):
            board[i][j] = q[i]
    return board

def moveHorizontal(board, s, step):
    #  왼쪽: board, 0, 1
    # 오른쪽: board, n - 1, -1
    global maxBlock
    # 0. 빈 공간 지우기
    if step == 1:
        start, end = 0, n
    else:
        start, end = n - 1, -1

    for i in range(n):
        q = [0] * n
        k = s
        for j in range(start, end, step):
            if board[i][j] != 0:
                q[k] = board[i][j]
                k += step
        for j in range(n):
            board[i][j] = q[j]
            
    # 1. 블록 합치기
    for i in range(n):
        j = s
        while (step == -1 and j > 0) or (step == 1 and j < n - 1):
            if board[i][j] == 0: # 현재 위치가 비어있을 때
                j += step
            else: # 현재 위치가 비어있지 않을 때
                if board[i][j] != board[i][j + step]: # 앞 블럭과 다른 블럭인 경우
                    j += step
                else: # 앞 블럭과 같은 블럭인 경우
                    board[i][j], board[i][j + step] = 0, board[i][j + step] * 2
                    maxBlock = max(maxBlock, board[i][j + step])
                    j += step * 2

    # 2. 빈 공간 지우기
    if step == 1:
        start, end = 0, n
    else:
        start, end = n - 1, -1

    for i in range(n):
        q = [0] * n
        k = s
        for j in range(start, end, step):
            if board[i][j] != 0:
                q[k] = board[i][j]
                k += step
        for j in range(n):
            board[i][j] = q[j]
    return board

def dfs(cnt, board):
    if cnt == 5:
        return

    dfs(cnt + 1, moveVertical(deepcopy(board), 0, 1)) # 위로
    dfs(cnt + 1, moveVertical(deepcopy(board), n - 1, -1)) # 아래로
    dfs(cnt + 1, moveHorizontal(deepcopy(board), 0, 1)) # 왼쪽으로
    dfs(cnt + 1, moveHorizontal(deepcopy(board), n - 1, -1)) # 오른쪽으로

def printBoard(board):
    print("-----")
    for i in range(n):
        print(*board[i])

def solution():
    global n, maxBlock
    n = int(input())
    board = []
    maxBlock = 0

    for i in range(n):
        board.append(list(map(int, input().split())))
        maxBlock = max(maxBlock, max(board[i]))

    dfs(0, board)
    return maxBlock

print(solution())
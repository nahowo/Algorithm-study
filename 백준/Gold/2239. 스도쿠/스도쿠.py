import sys
input = sys.stdin.readline

def firstEmpty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

def check(c, r, fill):
    for i in range(9):
        if board[c][i] == fill or board[i][r] == fill:
            return False
    
    for i in range(c // 3 * 3, c // 3 * 3 + 3):
        for j in range(r // 3 * 3, r // 3 * 3 + 3):
            if board[i][j] == fill:
                return False
    return True

def backtracking():
    try:
        c, r = firstEmpty()
    except:
        return True
    
    for fill in range(1, 10):
        if check(c, r, fill):
            board[c][r] = fill
            if backtracking():
                return True
            else:
                board[c][r] = 0
    return False

def solution():
    global board
    board = []
    for _ in range(9):
        board.append(list(map(int, list(str(input().rstrip())))))
    
    backtracking()
    
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = "")
        print()
    return

solution()
import sys
from collections import deque
input = sys.stdin.readline
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def move(x, y):
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[nx][ny] == '*':
                return False
            nx += dx
            ny += dy
    return True

def solution():
    global board
    board = []
    queens = []
    for i in range(8):
        tmp = input().rstrip()
        for j in range(8):
            if tmp[j] == '*':
                queens.append((i, j))
        board.append(tmp)
    
    if len(queens) < 8:
        return "invalid"

    for x, y in queens:
        if move(x, y) == False:
            return "invalid"
    return "valid"

print(solution())
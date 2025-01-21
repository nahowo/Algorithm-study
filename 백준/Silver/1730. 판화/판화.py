import sys
input = sys.stdin.readline
d = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
char = {'U': '|', 'D': '|', 'L': '-', 'R': '-'}

def carve(current, move):
    answer = ''
    if current != move and current != '.':
        answer = '+'
    else:
        answer = move
    return answer

def solution():
    global n
    n = int(input())
    move = input().rstrip()
    
    board = [['.'] * (n) for _ in range(n)]
    x, y = 0, 0
    for m in move:
        dx, dy = d[m]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            board[x][y] = carve(board[x][y], char[m])
            board[nx][ny] = carve(board[nx][ny], char[m])
            x, y = nx, ny
    
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = '')
        print()
    return

solution()
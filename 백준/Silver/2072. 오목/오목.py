import sys
input = sys.stdin.readline
d = {"horizontal": [(0, 1), (0, -1)], "vertical": [(1, 0), (-1, 0)], "rightDiagonal": [(1, 1), (-1, -1)], "leftDiagonal": [(1, -1), (-1, 1)]}
inRange = lambda x, y: 0 <= x < 19 and 0 <= y < 19

def solution():
    global board
    n = int(input())
    answer = -1
    board = [['' for _ in range(19)] for _ in range(19)]
    for cnt in range(1, n + 1):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if answer != -1:
            continue
        color = cnt % 2
        board[i][j] = color
        if check(i, j, color):
            answer = cnt
    return answer

def check(i, j, color):
    if count5(i, j, color, d["horizontal"]) or count5(i, j, color, d["vertical"]) or count5(i, j, color, d["rightDiagonal"]) or count5(i, j, color, d["leftDiagonal"]):
        return True
   
def count5(i, j, color, direction):
    count = 1
    for di, dj in direction:
        ni, nj = i + di, j + dj
        while inRange(ni, nj) and board[ni][nj] == color:
            count += 1
            if count > 5:
                return False
            ni += di
            nj += dj
    if count == 5:
        return True
    return False

print(solution())
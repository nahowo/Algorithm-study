import sys
input = sys.stdin.readline

def checkVertical(n, grid): # 세로줄 확인
    s = [False] * 10
    for i in range(9):
        if not s[grid[i][n]]:
            s[grid[i][n]] = True
        else:
            return False
    return True

def checkHorizontal(n, grid): # 가로줄 확인
    s = [False] * 10
    for i in range(9):
        if not s[grid[n][i]]:
            s[grid[n][i]] = True
        else:
            return False
    return True

def checkSquare(x, y, grid): # 3 * 3 네모 확인
    s = [False] * 10
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if not s[grid[i][j]]:
                s[grid[i][j]] = True
            else:
                return False
    return True

def solution():
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().split())))
    
    for i in range(9):
        for j in range(9):
            if not checkVertical(i, grid) or not checkHorizontal(j, grid):
                return False
            if i % 3 == 0 and j % 3 == 0:
                if not checkSquare(i, j, grid):
                    return False
    return True

t = int(input())
for i in range(1, t + 1):
    if not solution():
        print("Case " + str(i) + ": INCORRECT")
    else:
        print("Case " + str(i) + ": CORRECT")
    input()
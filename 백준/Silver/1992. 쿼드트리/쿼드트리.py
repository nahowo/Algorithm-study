import sys
input = sys.stdin.readline

def checkString(n, sx, sy, ex, ey):
    flag = string[sx][sy]
    for i in range(sx, ex):
        for j in range(sy, ey):
            if string[i][j] != flag:
                return False
    
    return flag

def recursion(n, sx, sy, ex, ey):
    global composed
    if n == 1:
        composed += string[sx][sy]
        return

    tmpString = checkString(n, sx, sy, ex, ey)
    if tmpString == False:
        composed += "("
        recursion(n // 2, sx, sy, sx + n // 2, sy + n // 2)
        recursion(n // 2, sx, sy + n // 2, sx + n // 2, sy + n)
        recursion(n // 2, sx + n // 2, sy, sx + n, sy + n // 2)
        recursion(n // 2, sx + n // 2, sy + n // 2, sx + n, sy + n)
        composed += ")"
    else:
        composed += tmpString
    

def solution():
    global string, composed
    n = int(input())
    string = [input().rstrip() for _ in range(n)]
    composed = ""
    recursion(n, 0, 0, n, n)
    return composed

print(solution())
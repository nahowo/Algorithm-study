import sys
input = sys.stdin.readline

def isBlack(a, size):
    if (n - k) // 2 * size <= a < (n + k) // 2 * size:
        return 1

def checkColor(r, c, size):
    if isBlack(r, size) and isBlack(c, size):
        return 1
    return 0

def getValue(r, c, time):
    if time == 0:
        return 0
    if time == 1:
        return checkColor(r, c, time)
    
    size = n ** (time - 1) # 작은 단위 길이
    if checkColor(r, c, size):
        return 1
    return getValue(r % size, c % size, time - 1)

def solution():
    global n, k
    s, n, k, r1, r2, c1, c2 = map(int, input().split())
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            print(getValue(i, j, s), end='')
        print()

solution()
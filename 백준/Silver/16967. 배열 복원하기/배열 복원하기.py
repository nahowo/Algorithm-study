import sys
input = sys.stdin.readline

def solution():
    h, w, x, y = map(int, input().split())
    bTable = []

    for _ in range(h):
        bTable.append(list(map(int, input().split()[:w])))
    
    for i in range(h - x):
        for j in range(w - y):
            bTable[i + x][j + y] -= bTable[i][j]
    
    for i in range(h):
        print(' '.join(map(str, bTable[i])))

solution()
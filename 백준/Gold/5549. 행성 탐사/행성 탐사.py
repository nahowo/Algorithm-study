import sys
input = sys.stdin.readline

def makeCSum(target):
    cSum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cSum[i][j] = cSum[i][j - 1]
            if maps[i - 1][j - 1] == target:
                cSum[i][j]+= 1
    for i in range(2, m + 1):
        for j in range(1, n + 1):
            cSum[i][j] += cSum[i - 1][j]
    return cSum

def checkCnt(a, b, c, d, cSum):
    ret = cSum[c][d] - (cSum[c][b - 1]) - (cSum[a - 1][d] - cSum[a - 1][b - 1])
    return ret

def solution():
    global m, n, maps
    m, n = map(int, input().split())
    k = int(input())
    maps = [input().rstrip() for _ in range(m)]
    research = [list(map(int, input().split())) for _ in range(k)]

    jungle = makeCSum('J')
    ocean = makeCSum('O')
    ice = makeCSum('I')
    for a, b, c, d in research:
        jCnt = checkCnt(a, b, c, d, jungle)
        oCnt = checkCnt(a, b, c, d, ocean)
        iCnt = checkCnt(a, b, c, d, ice)
        print(jCnt, oCnt, iCnt)
    return

solution()
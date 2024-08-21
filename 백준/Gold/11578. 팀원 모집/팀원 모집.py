import sys
input = sys.stdin.readline

def makeSet(s, check, startPoint):
    global minCnt
    if len(s) == n:
        minCnt = min(minCnt, len(check))
        return

    for i in range(startPoint, m + 1):
        if i not in check:
            makeSet(s | student[i], check | {i}, i + 1) # 현재값을 넣은 경우
            makeSet(s, check, i + 1) # 현재값을 넣지 않은 경우
    return

def solution():
    global n, m, minCnt, student
    n, m = map(int, input().split())
    minCnt = sys.maxsize
    student = dict()
    
    for i in range(1, m + 1):
        tmp = list(map(int, input().split()))
        student[i] = set(tmp[1:])
    
    makeSet(set(), set(), 1)

solution()
if minCnt < sys.maxsize:
    print(minCnt)
else:
    print(-1)
import sys
input = sys.stdin.readline

def makeNumber(n, cnt, l):
    if cnt == l:
        numbers.add(n)
        return
    
    for i in range(k):
        makeNumber(n * 10 + ks[i], cnt + 1, l)

def solution():
    global k, numbers, ks
    n, k = map(int, input().split())
    ks = list(map(int, input().split()))
    numbers = set()
    for l in range(len(str(n)) - 1, len(str(n)) + 1):
        makeNumber(0, 0, l)
    
    maxNum = 0
    for i in numbers:
        if i <= n:
            maxNum = max(maxNum, i)
    return maxNum

print(solution())
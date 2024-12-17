import sys
input = sys.stdin.readline

def makeComb(a, b):
    comb = dict()
    for i in range(n):
        for j in range(n):
            comb[a[i] + b[j]] = comb.get(a[i] + b[j], 0) + 1
    return comb

def checkComb(a, b, comb):
    cnt = 0
    for i in range(n):
        for j in range(n):
            tmp = -1 * (a[i] + b[j])
            if tmp in comb:
                cnt += comb[tmp]
    return cnt

def solution():
    global n
    n = int(input())
    a = []
    b = []
    c = []
    d = []
    for _ in range(n):
        ta, tb, tc, td = map(int, input().split())
        a.append(ta)
        b.append(tb)
        c.append(tc)
        d.append(td)
    
    comb = makeComb(a, b)
    return checkComb(c, d, comb)

print(solution())
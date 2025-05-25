import sys
input = sys.stdin.readline

def rec(i):
    if i <= 0:
        return 1
    if i in a:
        return a[i]
    
    ret = rec(i // p - x) + rec(i // q - y)
    a[i] = ret
    return ret

def solution():
    global a, n, p, q, x, y
    n, p, q, x, y = map(int, input().split())
    a = dict()
    return rec(n)

print(solution())
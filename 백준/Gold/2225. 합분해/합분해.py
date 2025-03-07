import sys
input = sys.stdin.readline
DIV = 10 ** 9

def rec(k, n):
    if k == 1:
        return 1
    if k == 2:
        return n + 1
    if n == 0:
        return 1
    if cache[k][n] != -1:
        return cache[k][n]
    
    ret = 0
    for i in range(0, n + 1):
        ret += rec(k - 1, n - i) % DIV
    cache[k][n] = ret % DIV
    return cache[k][n]

def solution():
    global cache
    n, k = map(int, input().split())
    cache = [[-1] * (n + 1) for _ in range(k + 1)]
    return rec(k, n)

print(solution())
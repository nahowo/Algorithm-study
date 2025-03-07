import sys
input = sys.stdin.readline

def rec(n):
    if n < 0:
        return 0
    if cache[n] != -1:
        return cache[n]
    
    ret = 3 * rec(n - 2)
    for i in range(4, n + 3, 2):
        ret += 2 * rec(n - i)
    cache[n] = ret
    return ret

def solution():
    global cache
    n = int(input())
    if n % 2 == 1:
        return 0
    cache = [-1] * (n + 4)
    cache[0] = 1
    cache[2] = 3
    return rec(n)

print(solution())
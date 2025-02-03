import sys
input = sys.stdin.readline

def recursion(n):
    if cache[n] != -1:
        return cache[n]
    
    ret = 0
    for i in range(n + 1, N):
        if a[n] < a[i]:
            ret = recursion(i)
            cache[n] = max(cache[n], ret + a[n])
    cache[n] = max(cache[n], a[n])
    return cache[n]

def solution():
    global a, cache, N, maxSum
    N = int(input())
    a = list(map(int, input().split()))
    maxSum = [0] * N
    cache = [-1] * N
    for i in range(N):
        recursion(i)
    return max(cache)

print(solution())
import sys
input = sys.stdin.readline

def recursion(n):
    if cache[n] != -1:
        return cache[n]
    
    ret = 0
    for i in range(n + 1, N):
        if a[i] > a[n]:
            ret = max(ret, recursion(i))
    ret += a[n]
    cache[n] = ret
    return cache[n]

def solution():
    global a, cache, N, maxSum
    N = int(input()) + 1
    a = [0] + list(map(int, input().split())) # 모든 경우의 수를 탐색하기 위해 패딩
    maxSum = [0] * N
    cache = [-1] * N
    recursion(0)
    return max(cache)

print(solution())
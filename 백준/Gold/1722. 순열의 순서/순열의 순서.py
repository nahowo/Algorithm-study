import sys
input = sys.stdin.readline

def factorial(n):
    cache = [0] * (n + 1)
    result = 1
    for i in range(1, n + 1):
        result *= i
        cache[i] = result
    return cache

def getPerm(k, n, cache): # 1
    perm = [0] * n
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1): # 현재 구성하려는 수열 위치
        for j in range(1, n + 1): # 수열 요소
            if not visited[j]:
                if k <= cache[n - i] or k == 1:
                    perm[i - 1] = j
                    visited[j] = True
                    break
                elif k > cache[n - i]:
                    k -= cache[n - i]

    return perm
    
def getK(perm, n, cache): # 2
    k = 1
    p = list(range(1, n + 1)) # 남아있는 수열 요소
    for i in range(1, n + 1):
        idx = p.index(perm[i - 1])
        k += idx * cache[n - i]
        p.remove(perm[i - 1])
    return [k]

def solution():
    n = int(input())
    cache = factorial(n)

    q = list(map(int, input().split()))
    num = q[0]
    answer = 0
    if num == 1:
        answer = getPerm(q[1], n, cache)
    else:
        answer = getK(q[1:], n, cache)
    return answer

print(*solution())
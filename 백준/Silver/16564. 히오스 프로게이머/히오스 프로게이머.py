import sys
input = sys.stdin.readline

def calcCost(x, n, targetHeight):
    cost = 0
    for i in range(n):
        cost += max(0, targetHeight - x[i])
    return cost

def solution():
    n, k = map(int, input().split())
    x = [int(input()) for _ in range(n)]

    start = min(x)
    end = max(x) + k
    
    t = start
    while start <= end:
        mid = (start + end) // 2
        if calcCost(x, n, mid) > k:
            end = mid - 1
        else:
            t = mid
            start = mid + 1
    return t

print(solution())
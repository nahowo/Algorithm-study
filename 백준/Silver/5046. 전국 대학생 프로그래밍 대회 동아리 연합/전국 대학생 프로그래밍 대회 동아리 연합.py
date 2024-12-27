import sys
input = sys.stdin.readline

def solution():
    n, b, h, w = map(int, input().split())
    minCost = sys.maxsize
    for _ in range(h):
        p = int(input())
        available = list(map(int, input().split()))
        for j in range(w):
            if n <= available[j]:
                minCost = min(minCost, n * p)

    if minCost <= b:
        return minCost
    return "stay home"
    
print(solution())
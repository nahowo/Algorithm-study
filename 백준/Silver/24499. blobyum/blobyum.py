import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    pie = list(map(int, input().split()))
    maxS = 0
    tmpS = sum(pie[:k])
    for i in range(k, k + n):
        start = i - k
        end = i % n
        maxS = max(maxS, tmpS)
        tmpS -= pie[start]
        tmpS += pie[end]
    return maxS
    
print(solution())
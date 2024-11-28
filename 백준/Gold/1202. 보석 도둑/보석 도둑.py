import sys
import heapq
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    gems = []
    for _ in range(n):
        m, v = map(int, input().split())
        gems.append([m, -v]) # 무게, 가격 * -1    
    
    bags = []
    for _ in range(k):
        bags.append(int(input()))
    
    heapq.heapify(gems)
    bags.sort()
    canSteal = []
    totalV = 0

    for i in range(k):
        while gems and gems[0][0] <= bags[i]:
            heapq.heappush(canSteal, heapq.heappop(gems)[1])
        if canSteal:
            totalV -= heapq.heappop(canSteal)
    
    return totalV

print(solution())
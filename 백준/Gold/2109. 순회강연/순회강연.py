import sys, heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    if n == 0:
        return 0
    request = dict()
    for _ in range(n):
        p, d = map(int, input().split())
        if d in request:
            request[d].append(p)
        else:
            request[d] = [p]

    q = []
    totalPay = 0
    for i in range(max(request.keys()), 0, -1):
        if i in request:
            for j in request[i]:
                heapq.heappush(q, -j)
        if q:
            totalPay += -heapq.heappop(q)
    
    return totalPay

print(solution())
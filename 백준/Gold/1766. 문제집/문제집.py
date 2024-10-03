import sys, heapq
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    connected = {i: set() for i in range(1, n + 1)} # i: {i를 선수로 가지는 문제들}
    inEdge = {i: 0 for i in range(1, n + 1)} # i: i 문제의 진입간선 수
    
    for _ in range(m):
        a, b = map(int, input().split())
        connected[a].add(b)
        inEdge[b] += 1
    
    inCnt = {i: set() for i in range(0, n)} # i: [진입간선이 i개인 문제들]
    for i in range(1, n + 1):
        inCnt[inEdge[i]].add(i)
    
    order = []
    q = []
    for i in inCnt[0]:
        q.append(i)
    heapq.heapify(q)

    while q:
        x = heapq.heappop(q)
        order.append(x)
        for cx in connected[x]:
            cnt = inEdge[cx]
            inCnt[cnt].remove(cx)
            inCnt[cnt - 1].add(cx)
            inEdge[cx] -= 1
            if inEdge[cx] == 0:
                heapq.heappush(q, cx)
    return order

print(*solution())
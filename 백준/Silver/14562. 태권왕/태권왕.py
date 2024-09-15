import sys, heapq
input = sys.stdin.readline

def solution():
    s, t = map(int, input().split())

    # 백트래킹
    q = [(0, s, t)]
    while q:
        cnt, s, t = heapq.heappop(q)
        
        if s == t:
            return cnt
        elif s > t:
            continue
        else:
            heapq.heappush(q, (cnt + 1, s * 2, t + 3))
            heapq.heappush(q, (cnt + 1, s + 1, t))

t = int(input())
for _ in range(t):
    print(solution())
import sys
input = sys.stdin.readline
import heapq

def solution():
    n, h, t = map(int, input().split())
    giant = []
    for _ in range(n):
        giant.append(-int(input()))
    heapq.heapify(giant)

    cnt = 0
    for i in range(t + 1):
        x = heapq.heappop(giant)
        if -x < h:
            print("YES")
            print(i)
            return
        if -x == 1:
            heapq.heappush(giant, -1)
        else:
            heapq.heappush(giant, -((-x) // 2))
    print("NO")
    print(-x)

solution()
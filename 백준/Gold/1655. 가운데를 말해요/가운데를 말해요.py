import sys
import heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    small = [] # 작은 절반
    big = [] # 큰 절반
    ls, lb = 0, 0

    for i in range(1, n + 1):
        x = int(input())
        if ls == 0:
            heapq.heappush(small, -x)
            ls += 1
        elif -small[0] >= x:
            heapq.heappush(small, -x)
            ls += 1
        else:
            heapq.heappush(big, x)
            lb += 1

        if i % 2 == 0:
            if ls == lb + 2:
                heapq.heappush(big, (-1) * heapq.heappop(small))
                ls -= 1
                lb += 1
        else:
            if lb == ls + 1:
                heapq.heappush(small, (-1) * heapq.heappop(big))
                ls += 1
                lb -= 1
        
        print(-small[0])

solution()
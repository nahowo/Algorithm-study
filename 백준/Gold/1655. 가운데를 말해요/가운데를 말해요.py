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
        while True:
            if (i % 2 == 0 and ls == lb) or (i % 2 == 1 and ls == lb + 1):
                break
            if i % 2 == 0: # 수의 개수가 짝수: ls == lb여야 함
                if lb > ls:
                    while lb > ls:
                        heapq.heappush(small, (-1) * heapq.heappop(big))
                        ls += 1
                        lb -= 1
                elif ls > lb:
                    while ls > lb:
                        heapq.heappush(big, (-1) * heapq.heappop(small))
                        ls -= 1
                        lb += 1
            else: # 수의 개수가 홀수: ls == lb + 1이여야 함
                if lb >= ls:
                    while lb >= ls:
                        heapq.heappush(small, (-1) * heapq.heappop(big))
                        ls += 1
                        lb -= 1
                elif ls > lb + 1:
                    while ls > lb + 1:
                        heapq.heappush(big, (-1) * heapq.heappop(small))
                        ls -= 1
                        lb += 1
        print(-small[0])

solution()
import sys
import heapq
input=sys.stdin.readline

n=int(input())
arr=[]
a=[]
for i in range(n):
    integer=int(input())
    if integer>0:
        heapq.heappush(arr,integer)
    else:
        if len(arr)>0:
            print(heapq.heappop(arr))
        else:
            print(0)
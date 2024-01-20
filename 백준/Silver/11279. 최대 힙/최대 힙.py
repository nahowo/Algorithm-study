import sys
import heapq
input=sys.stdin.readline

def func():
    n=int(input())
    arr=[]
    for i in range(n):
        tmp=int(input())
        if tmp>0:
            heapq.heappush(arr,tmp*(-1))
        else:
            if len(arr)==0:
                print(0)
            else:
                target=heapq.heappop(arr)
                print(target*(-1))

func()
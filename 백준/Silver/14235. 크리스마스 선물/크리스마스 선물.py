import sys
import heapq
input=sys.stdin.readline

def func():
    n=int(input())
    h=[]
    for _ in range(n):
        a=list(map(int,input().split()))
        if a[0]==0: # 아이들 방문
            if len(h)==0:
                print(-1)
            else:
                print(heapq.heappop(h)*(-1)) # 최대값 출력
        else: # 거점지 방문
            for i in range(1,a[0]+1):
                heapq.heappush(h,a[i]*(-1))

func()
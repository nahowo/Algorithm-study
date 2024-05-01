import sys
from collections import deque
import heapq
input=sys.stdin.readline

def func():
    INF=10e9
    n=int(input())
    m=int(input())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append([b,c])
    s,e=map(int,input().split())
    dist=[INF]*(n+1)
    near=[s]*(n+1)

    q=[]
    heapq.heappush(q,[0,s])
    while q:
        d,x=heapq.heappop(q)
        if dist[x]<d:
            continue
        for nx,nd in graph[x]:
            cost=d+nd
            if cost<dist[nx]:
                dist[nx]=cost
                near[nx]=x
                heapq.heappush(q,[cost,nx])

    route=[]
    tmp=e
    while tmp!=s:
        route.append(tmp)
        tmp=near[tmp]
    route.append(s)
    
    print(dist[e])
    print(len(route))
    print(*route[::-1])

func()
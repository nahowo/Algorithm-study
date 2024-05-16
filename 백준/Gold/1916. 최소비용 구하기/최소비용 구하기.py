import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

def func():
    n=int(input())
    m=int(input())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append([b,c])
    s,e=map(int,input().split())
    costs=[INF]*(n+1)
    costs[s]=0
    q=[]
    heapq.heappush(q,[s,0])

    while q:
        x,cost=heapq.heappop(q)
        if costs[x]<cost: # 갱신하지 않아도 되는 경우
            continue
        for nx,ncost in graph[x]: # 연결 노드 탐색
            scost=cost+ncost
            if scost<costs[nx]: # 연결 노드 비용 업데이트
                costs[nx]=scost
                heapq.heappush(q,[nx,scost])
    return costs[e]
        
print(func())
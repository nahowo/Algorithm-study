import sys
import heapq
input=sys.stdin.readline
INF=10e9

def func():
    global graph
    n,e=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(e):
        a,b,c=map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])
    v1,v2=map(int,input().split())
    dist=[INF]*(n+1)
    
    route1=dijkstra(1,v1,dist.copy())+dijkstra(v1,v2,dist.copy())+dijkstra(v2,n,dist.copy()) # 1 -> v1 -> v2 -> n
    route2=dijkstra(1,v2,dist.copy())+dijkstra(v2,v1,dist.copy())+dijkstra(v1,n,dist.copy()) # 1 -> v2 -> v1 -> n
    route=min(route1,route2)
    if route>=INF:
        return -1
    else:
        return route

def dijkstra(s,e,dist):
    q=[]
    heapq.heappush(q,[0,s])
    dist[s]=0
    while q:
        d,x=heapq.heappop(q)
        if dist[x]<d:
            continue
        for nx,nd in graph[x]:
            cost=d+nd
            if cost<dist[nx]:
                dist[nx]=cost
                heapq.heappush(q,[cost,nx])
    return dist[e]

print(func())
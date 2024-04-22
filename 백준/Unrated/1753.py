# import heapq
# import sys
# input=sys.stdin.readline
# def dijkstra(start):
#     q=[]
#     heapq.heappush(q,(start,0))
#     dist[start]=0
#     while q:
#         now_v,d=heapq.heappop(q)
#         if dist[now_v]<d:
#             continue
#         for v,w in graph[now_v]: #now_v와 연결된 정점, 가중치
#             cost=d+w
#             if cost<dist[v]: #기존 비용보다 더 적게 드는 경우
#                 dist[v]=cost
#                 heapq.heappush(q,(v,cost))
# v,e=map(int,input().split())
# start=int(input())
# INF=10**9
# dist=[INF]*(v+1)
# graph=[[] for _ in range(v+1)]
# for i in range(e):
#     u,v,w=map(int,input().split())
#     graph[u].append((v,w))
# dijkstra(start)
# for n in dist[1:]:
#     if n!=INF:
#         print(n)
#     else:
#         print("INF")
import heapq
import sys
input=sys.stdin.readline
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        d,now_v=heapq.heappop(q)
        if dist[now_v]<d:
            continue
        for v,w in graph[now_v]:
            cost=d+w
            if cost<dist[v]:
                dist[v]=cost
                heapq.heappush(q,(cost,v))
v,e=map(int,input().split())
start=int(input())
INF=10**9
dist=[INF]*(v+1)
graph=[[] for _ in range(v+1)]
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((v, w))
dijkstra(start)
for n in dist[1:]:
    if n!=INF:
        print(n)
    else:
        print("INF")
import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

def func(s):
    distance=[INF]*(n+1)
    distance[s]=0
    q=[]
    heapq.heappush(q,[s,0])
    item=0 # 얻을 수 있는 아이템 개수

    while q:
        x,dist=heapq.heappop(q)
        if distance[x]<dist: # 갱신하지 않아도 되는 경우
            continue
        for nx,ndist in graph[x]: # 연결 노드 탐색
            sdist=dist+ndist
            if sdist<distance[nx]: # 연결 노드 비용 업데이트
                distance[nx]=sdist
                heapq.heappush(q,[nx,sdist])
    
    for i in range(1,n+1):
        if distance[i]<=m:
            item+=t[i]
    return item

n,m,r=map(int,input().split())
t=[0]+list(map(int,input().split())) # 0 인덱스 패딩 추가
graph=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

answer=[]
for i in range(1,n+1):
    answer.append(func(i))
print(max(answer))
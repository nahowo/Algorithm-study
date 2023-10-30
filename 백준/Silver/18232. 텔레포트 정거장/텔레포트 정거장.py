import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
s,e=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m): # 텔레포트 가능 지점 추가
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

INF=int(1e7)
shortest=[0]+[INF]*n # 최단 거리 리스트를 모두 무한으로 초기화
shortest[s]=0
q=deque([s])

while q:
    x=q.popleft()
    current_time=shortest[x]
    if x==e:
        break # 도착점 도달 시 종료
    for i in x+1, x-1:
        if 1<=i<=n and shortest[i]>shortest[x]+1: 
            q.append(i)
            shortest[i]=shortest[x]+1
    
    for nx in graph[x]:
        if shortest[nx]>current_time:
            shortest[nx]=current_time+1 # 기존 거리보다 짧은 경우에만 방문, 업데이트
            q.append(nx)
print(shortest[e]) # 도착점의 최단 거리 출력
import sys
from collections import deque
input=sys.stdin.readline
c=int(input())
connect=int(input())
network=[[] for _ in range(c+1)]
for _ in range(connect):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)
infected=0
visited=[False]*(c+1)
def dfs():
    global infected
    q=deque()
    q.append(1)
    visited[1]=True
    while q:
        x=q.pop()
        for i in network[x]:
            if visited[i]==False:
                infected+=1
                visited[i]=True #방문 처리
                q.append(i)
dfs()
print(infected)
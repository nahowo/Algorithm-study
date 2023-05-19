import sys
from collections import deque
input=sys.stdin.readline
def bfs(s,f):
    q=deque()
    q.append((s,0))
    visited=[0]*(n+1)
    visited[s]=1
    while q:
        v,d=q.popleft()
        if v==f:
            return d
        for i,l in graph[v]:
            if visited[i]==0:
                visited[i]=1
                q.append((i,d+l))
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    tmp1,tmp2,l=map(int,input().split())
    graph[tmp1].append((tmp2,l))
    graph[tmp2].append((tmp1,l))
for i in  range(m):
    n1,n2=map(int,input().split())
    print(bfs(n1,n2))
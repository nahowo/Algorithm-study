import sys
from collections import deque
input=sys.stdin.readline

def func():
    n=int(input())
    graph=[[] for _ in range(n+1)]
    for i in range(n-1):
        tmp=list(map(int,input().split()))
        graph[tmp[0]].append([tmp[1],tmp[2]])
        graph[tmp[1]].append([tmp[0],tmp[2]])
    
    a,b=dfs(1,graph,n)
    L,answer=dfs(b,graph,n)
    return L

def dfs(s,graph,v):
    tmpL=0
    tmpAnswer=0
    q=deque()
    visited=[False]*(v+1)
    q.append([s,0])
    visited[s]=True

    while q:
        x,l=q.pop()
        if l>tmpL:
            tmpL=l
            tmpAnswer=x
        for nx,nl in graph[x]:
            if not visited[nx]:
                visited[nx]=True
                q.append([nx,l+nl])
    return tmpL,tmpAnswer

print(func())
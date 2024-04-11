import sys
from collections import deque
input=sys.stdin.readline

def func():
    v=int(input())
    graph=[[] for _ in range(v+1)]
    for i in range(v):
        tmp=list(map(int,input().split()))
        for j in range(1,len(tmp),2):
            if tmp[j]==-1:
                break
            graph[tmp[0]].append([tmp[j],tmp[j+1]])
    
    a,b=dfs(1,graph,v)
    L,answer=dfs(b,graph,v)
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
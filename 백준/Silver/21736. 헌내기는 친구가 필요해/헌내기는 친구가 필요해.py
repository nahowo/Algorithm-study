import sys
from collections import deque
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    graph=[]
    d=[[1,0],[-1,0],[0,1],[0,-1]]
    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        graph.append(input().rstrip())
        for j in range(m):
            if graph[i][j]=="I":
                sx,sy=i,j
    q=deque()
    q.append([sx,sy])
    friends=0
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]=='P':
                    friends+=1
                    q.append([nx,ny])
                elif graph[nx][ny]=='O':
                    q.append([nx,ny])
                visited[nx][ny]=True
    return friends if friends>0 else "TT"

print(func())
import sys
from collections import deque
input=sys.stdin.readline

X,Y,n=map(int,input().split())
X+=500
Y+=500
graph=[[0]*(1001) for _ in range(1001)]
graph[500][500]=1
d=[(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(n):
    a,b=map(int,input().split())
    graph[a+500][b+500]=2

def func():
    q=deque()
    q.append([500,500])
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if nx==X and ny==Y:
                return graph[x][y]
            if 0<=nx<=1000 and 0<=ny<=1000 and not graph[nx][ny]:
                graph[nx][ny]=graph[x][y]+1
                q.append([nx,ny])
                
print(func())
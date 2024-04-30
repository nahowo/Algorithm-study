import sys
from collections import deque
input=sys.stdin.readline

def func():
    d=[[1,0],[-1,0],[0,1],[0,-1]]
    graph=[['0']*501 for _ in range(501)]
    n=int(input()) # 위험한 구역: '1'
    for _ in range(n):
        x1,y1,x2,y2=map(int,input().split())
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                graph[i][j]='1'
    
    m=int(input()) # 죽음의 구역: '2'
    for _ in range(m):
        x1,y1,x2,y2=map(int,input().split())
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                graph[i][j]='2'
    
    if graph[500][500]=='2': # 목적지가 죽음의 구역일 때
        return -1

    q=deque()
    q.append([0,0])
    graph[0][0]=0
    flag=False
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<=500 and 0<=ny<=500:
                if graph[nx][ny]=='0':
                    q.appendleft([nx,ny])
                    graph[nx][ny]=graph[x][y]
                elif graph[nx][ny]=='1':
                    q.append([nx,ny])
                    graph[nx][ny]=graph[x][y]+1
                if nx==500 and ny==500:
                    flag=True
                    break
    if not flag:
        return -1
    return graph[500][500]

print(func())
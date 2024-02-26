import sys
from collections import deque
input=sys.stdin.readline

def func():
    m,n,h=map(int,input().split())
    box=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
    d=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
    q=deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k]==1:
                    q.append([i,j,k])

    while q:
        z,y,x=q.popleft() # x-m, y-n, z-h
        for dx,dy,dz in d:
            nx,ny,nz=dx+x,dy+y,dz+z
            if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                if box[nz][ny][nx]==0:
                    box[nz][ny][nx]=box[z][y][x]+1
                    q.append([nz,ny,nx])
    
    day=0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k]==0:
                    return -1
                day=max(day,box[i][j][k])
    return day-1
    
print(func())
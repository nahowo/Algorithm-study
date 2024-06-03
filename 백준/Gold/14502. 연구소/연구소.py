import sys
from collections import deque
import copy
input=sys.stdin.readline
d=[[1,0],[-1,0],[0,1],[0,-1]]

def buildWall(cnt):
    global maxSafePlace
    if cnt==3:
        tmplab=bfs()
        maxSafePlace=max(maxSafePlace,countSafe(tmplab))
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j]==0:
                lab[i][j]=1
                buildWall(cnt+1)
                lab[i][j]=0

def bfs():
    q=copy.deepcopy(virus)
    tmplab=copy.deepcopy(lab)
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and tmplab[nx][ny]==0:
                tmplab[nx][ny]=2
                q.append([nx,ny])
    return tmplab

def countSafe(tmplab):
    safePlace=0
    for i in range(n):
        safePlace+=tmplab[i].count(0)
    return safePlace

n,m=map(int,input().split())
lab=[]
virus=deque()
for i in range(n):
    lab.append(list(map(int,input().split())))
    for j in range(m):
        if lab[i][j]==2:
            virus.append([i,j])

maxSafePlace=0
buildWall(0)
print(maxSafePlace)
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy):
    q=deque()
    q.append([sx,sy])
    visited[sx][sy]=True
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and image[nx][ny]==255:
                    visited[nx][ny]=True
                    q.append([nx,ny])
    return 1

d=[(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())
image=[[0]*(m) for _ in range(n)]
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)):
        image[i][j//3]+=tmp[j]
t=int(input())

for i in range(n):
    for j in range(m):
        if (image[i][j]/3)>=t:
            image[i][j]=255
        else:
            image[i][j]=0

visited=[[False]*(m) for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(m):
        if image[i][j]==255 and not visited[i][j]:
            cnt+=bfs(i,j)
print(cnt)
import sys
input=sys.stdin.readline
from collections import deque
d=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
def dfs(sx,sy):
    q=deque()
    q.append([sx,sy])
    visited[sx][sy]=True
    while q:
        x,y=q.pop()
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if 0<=nx<h and 0<=ny<w:
                if map_[nx][ny]==1 and visited[nx][ny]==False:
                    q.append([nx,ny])
                    visited[nx][ny]=True
    return True
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    map_=[]
    visited=[[False]*w for _ in range(h)]
    cnt=0
    for _ in range(h):
        map_.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if map_[i][j]==1 and visited[i][j]==False: # 방문하지 않은 섬일 경우에만 함수 호출
                dfs(i,j)
                cnt+=1
    print(cnt)
import sys
from collections import deque
input=sys.stdin.readline
d=[(0,1),(0,-1),(1,0),(-1,0)]

def isAir():
    q=deque()
    q.append([0,0])
    air=[[False]*m for _ in range(n)] # 공기인 부분인지 아닌지 판별
    air[0][0]=True
    visited=[[False]*m for _ in range(n)]
    visited[0][0]=True

    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if paper[nx][ny]==0 and not visited[nx][ny]:
                    q.append([nx,ny])
                    air[nx][ny]=True
                    visited[nx][ny]=True
    return air

def checkMelt(i,j,airPaper):
    cnt=0
    for di,dj in d: # 공기와 접촉한 부분이 2변 이상인지 확인
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<m:
            if airPaper[ni][nj]==True:
                cnt+=1
                if cnt==2:
                    return True
    return False

n,m=map(int,input().split())
paper=[]
cheese=0
time=0
for i in range(n):
    paper.append(list(map(int,input().split())))
    cheese+=paper[i].count(1)

while cheese:
    airPaper=isAir()
    for i in range(n):
        for j in range(m):
            if paper[i][j]==1: # 치즈일 때
                if checkMelt(i,j,airPaper):
                    paper[i][j]=0 # 녹아서 공기로 변함
                    cheese-=1
    time+=1
print(time)
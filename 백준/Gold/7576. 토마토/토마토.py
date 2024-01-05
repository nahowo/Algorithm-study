import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
box=[]
for _ in range(n):
    box.append(list(map(int,input().split())))

q=deque()
days=0
d=[[1,0],[-1,0],[0,1],[0,-1]]

def check1(): # 익은 토마토 위치를 확인
    for i in range(n):
        for j in range(m):
            if box[i][j]==1:
                q.append([i,j])
    return False # 전부 안 익은 토마토일 경우

def check2(): # 토마토가 전부 익었는지 확인
    for i in range(n):
        for j in range(m):
            if box[i][j]==0:
                return False
    return True

check1()

while q:
    x,y=q.popleft()
    for dx,dy in d:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
            box[nx][ny]=box[x][y]+1
            q.append([nx,ny])

tmp=check2() # while문 이후 익지 못한 토마토가 있는지 확인
if not tmp:
    days=-1
else:
    for i in box:
        days=max(days,max(i)-1)

print(days)
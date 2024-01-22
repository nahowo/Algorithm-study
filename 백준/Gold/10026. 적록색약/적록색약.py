import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
paint_1=[]
paint_2=[]
for _ in range(n):
    tmp=input().rstrip()
    paint_1.append(tmp)
    tmp2=''
    for i in range(n):
        if tmp[i]=='R':
            tmp2+='G'
        else:
            tmp2+=tmp[i]
    paint_2.append(tmp2)

d=[[0,1],[0,-1],[1,0],[-1,0]]
visited=[[False]*n for _ in range(n)]
section_1=0
section_2=0

def func(sx,sy,p):
    if visited[sx][sy]:
        return False
    q=deque([])
    visited[sx][sy]=True
    q.append([sx,sy])

    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if p[nx][ny]==p[x][y]:
                    q.append([nx,ny])
                    visited[nx][ny]=True
    return True

for i in range(n):
    for j in range(n):
        if func(i,j,paint_1):
            section_1+=1

visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if func(i,j,paint_2):
            section_2+=1

print(section_1,section_2)
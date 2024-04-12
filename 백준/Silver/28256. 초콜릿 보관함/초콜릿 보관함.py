import sys
from collections import deque
input=sys.stdin.readline

def func():
    global box
    box=[]
    for _ in range(3):
        box.append(list(input().rstrip()))
    choco=list(map(int,input().split()))
    choco.pop(0)
    
    for i in range(3):
        for j in range(3):
            if box[i][j]=='O':
                cnt=bfs(i,j)
                if cnt in choco:
                    choco.remove(cnt)
                else:
                    return 0
    if len(choco)==0:
        return 1
    else:
        return 0

def bfs(sx,sy):
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.append([sx,sy])
    box[sx][sy]='X'
    cnt=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<3 and 0<=ny<3:
                if box[nx][ny]=='O':
                    box[nx][ny]='X'
                    q.append([nx,ny])
                    cnt+=1
    return cnt
    

t=int(input())
for i in range(t):
    print(func())
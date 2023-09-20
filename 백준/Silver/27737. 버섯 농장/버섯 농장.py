import sys
input=sys.stdin.readline
from collections import deque
d=[[0,1],[0,-1],[1,0],[-1,0]]
n,m,k=map(int,input().split())
farm=[]
for _ in range(n):
    tmp=list(map(str,input().split()))
    farm.append(tmp)
def bfs(sx,sy):
    global n
    q=deque([[sx,sy]])
    farm[sx][sy]='1'
    cnt=1
    while q:
        x,y=q.pop()
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<n:
                if farm[nx][ny]=='0':
                    farm[nx][ny]='1'
                    cnt+=1
                    q.appendleft([nx,ny])
    return cnt
mushroom=0
for i in range(n):
    for j in range(n):
        if farm[i][j]=='0':
            tmp=bfs(i,j)
            if tmp//k==tmp/k:
                mushroom+=tmp//k
            else:
                mushroom+=(tmp//k)+1
if m-mushroom>=0 and m!=m-mushroom:
    print('POSSIBLE')
    print(m-mushroom)
else:
    print('IMPOSSIBLE')
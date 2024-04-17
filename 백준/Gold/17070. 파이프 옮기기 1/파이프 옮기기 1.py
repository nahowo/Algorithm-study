import sys
input=sys.stdin.readline

def dfs(x,y,drx):
    global answer
    if x==n-1 and y==n-1:
        answer+=1
        return
    
    if drx!=1: # 가로로 이동
        ny=y+1
        if ny<n and house[x][ny]==0:
            dfs(x,ny,0)
    
    if drx!=0: # 세로로 이동
        nx=x+1
        if nx<n and house[nx][y]==0:
            dfs(nx,y,1)
    
    cnt=0
    for dx,dy in d: # 대각선으로 이동
        nx,ny=x+dx,y+dy
        if nx<n and ny<n and house[nx][ny]==0:
            cnt+=1
    if cnt==3:
        dfs(x+1,y+1,2)

n=int(input())
house=[]
for _ in range(n):
    house.append(list(map(int,input().split())))
d=[(0,1),(1,0),(1,1)]
answer=0

if house[n-1][n-1]==1:
    answer=0
else:
    dfs(0,1,0)
print(answer)
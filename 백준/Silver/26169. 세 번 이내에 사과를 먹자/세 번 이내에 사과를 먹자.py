import sys
input=sys.stdin.readline
board=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(5):
    board.append(list(map(int,input().split())))
r,c=map(int,input().split())
visited=[[False]*5 for _ in range(5)]
def dfs(x,y,cnt,apple):
    visited[x][y]=True
    if board[x][y]==1:
        apple+=1
    if apple>=2:
        return 1
    if cnt>2:
        visited[x][y]=False
        return 0
    for dx,dy in d:
        nx,ny=dx+x,dy+y
        if 0<=nx<5 and 0<=ny<5:
            if not visited[nx][ny] and board[nx][ny]!=-1:
                if dfs(nx,ny,cnt+1,apple)==1:
                    return 1
    visited[x][y]=False
    return 0
print(dfs(r,c,0,0))
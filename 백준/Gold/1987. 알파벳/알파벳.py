import sys
from collections import deque
input=sys.stdin.readline

r,c=map(int,input().split())
board=[]
for _ in range(r):
    board.append(list(input().rstrip()))
visited=set()
visited.add(board[0][0])
d=[(-1,0),(1,0),(0,1),(0,-1)]
answer=1

def dfs(x,y,l):
    global answer
    answer=max(answer,l)
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                dfs(nx,ny,l+1)
                visited.remove(board[nx][ny])

dfs(0,0,1)
print(answer)
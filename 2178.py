import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
d=[(1,0),(0,1),(-1,0),(0,-1)]
graph=[list(map(int,' '.join(input().split()))) for _ in range(n)]
def bfs():
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))
bfs()
print(graph[n-1][m-1])
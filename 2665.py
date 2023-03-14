from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
graph=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(n):
    graph.append(list(map(int,input().strip())))
visited=[[-1]*(n+1) for _ in range(n+1)]
def bfs():
    visited[0][0]=0
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                if graph[nx][ny]==1: #흰 방일때
                    visited[nx][ny]=visited[x][y]
                    q.appendleft((nx,ny)) #흰 방을 먼저 탐색하기 위해
                else: #검은 방일때
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1 #검은 방을 1개 부숨
bfs()
print(visited[n-1][n-1])
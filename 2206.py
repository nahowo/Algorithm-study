import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
d=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)] #지나온 방의 갯수를 세는 리스트
broke=[[0]*m for _ in range(n)] #부순 벽의 갯수를 세는 리스트
def bfs():
    q=deque()
    q.append([0,0,0])
    visited[0][0][0]=1
    while q:
        x,y,z=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visited[nx][ny][z]==0: #이동할 곳이 방문하지 않았고 벽이 없는 경우
                    visited[nx][ny][z]=visited[x][y][z]+1
                    q.append([nx,ny,z])
                elif graph[nx][ny]==1 and z==0: #방문할 곳이 벽이고 벽을 파괴하지 않은 경우
                    visited[nx][ny][1]=visited[x][y][z]+1
                    q.append([nx,ny,1])
    return -1
print(bfs())
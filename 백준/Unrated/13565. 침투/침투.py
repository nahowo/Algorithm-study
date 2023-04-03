import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
graph=[]
d=[(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(m):
    graph.append(input().rstrip())
def bfs(Y): #가로 정보만 입력받음(세로 시작은 0밖에 없으므로)
    visited=[[0]*n for _ in range(m)]
    if graph[0][Y]=='1':
        return 0
    q=deque()
    q.append((0,Y))
    visited[0][Y]=1
    while q:
        x,y=q.popleft()
        if x==m-1:
            return 1
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]=='0' and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
    return 0
for i in range(n):
    if bfs(i)==1:
        print('YES')
        exit(0)
print('NO')
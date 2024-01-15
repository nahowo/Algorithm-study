import sys
from collections import deque
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    graph=[]
    distance=[[0]*m for _ in range(n)]
    d=[[0,1],[0,-1],[1,0],[-1,0]]

    for i in range(n): # 지도 입력받고 거리 배열 초기화
        tmp=list(map(int,input().split()))
        graph.append(tmp)
        for j in range(m):
            if tmp[j]==2:
                init_pos=[i,j]
            distance[i][j]=sys.maxsize
    
    q=deque([init_pos])
    graph[init_pos[0]][init_pos[1]]=0
    distance[init_pos[0]][init_pos[1]]=0
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=dx+x,dy+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=0:
                q.append([nx,ny])
                graph[nx][ny]=0 # 방문처리
                tmpmin=[sys.maxsize]
                for tdx,tdy in d:
                    tnx,tny=tdx+nx,tdy+ny
                    if 0<=tnx<n and 0<=tny<m:
                        tmpmin.append(distance[tnx][tny])
                distance[nx][ny]=min(tmpmin)+1 # 상하좌우 중 최솟값+1

    for i in range(n):
        for j in range(m):
            if distance[i][j]==sys.maxsize: # 원래 갈 수 없는 위치
                distance[i][j]=0
            if graph[i][j]==1: # 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치
                distance[i][j]=-1
    return distance

res=func()
for i in res:
    print(*i)
import sys
input=sys.stdin.readline

t=int(input())
d=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
def func():
    n,m=map(int,input().split())
    team_id=[0]*101
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            if team_id[graph[i][j]]==0 and graph[i][j]!=-1:
                for dx, dy in d:
                    nx,ny=i+dx, j+dy
                    if 0<=nx<n and 0<=ny<m:
                        if graph[i][j]==graph[nx][ny]:
                            team_id[graph[i][j]]=1
    return team_id.count(1)
answer=[]
for _ in range(t):
    answer.append(func())
for i in answer:
    print(i)
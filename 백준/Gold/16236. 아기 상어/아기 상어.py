import sys
from collections import deque
input=sys.stdin.readline

d=[(1,0),(-1,0),(0,1),(0,-1)]

n=int(input())
babySharkSize=2
eatenFish=0
fish=dict()
for i in range(1,7):
    fish[i]=0

graph=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(n):
        if 1<=tmp[j]<=6: # 물고기 크기별 개수 저장
            fish[tmp[j]]+=1
        elif tmp[j]==9: # 아기상어 위치 저장, 초기화
            tmp[j]=0
            babySharkPos=[i,j]
    graph.append(tmp)

def bfs(sx,sy): # O(400)
    q=deque()
    q.append([sx,sy])
    visited=[[-1]*n for _ in range(n)]
    visited[sx][sy]=0
    
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                nxt=graph[nx][ny]
                if nxt<=babySharkSize and visited[nx][ny]==-1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
    return visited

def fish(visited):
    x,y=0,0
    mdist=10**9
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=-1 and 1<=graph[i][j]<babySharkSize:
                if visited[i][j]<mdist:
                    mdist=visited[i][j]
                    x,y=i,j
    if mdist==10**9:
        return False
    else:
        return x,y,mdist

def func():
    global babySharkSize, babySharkPos, eatenFish
    answer=0
    eatenFish=0

    while True:
        res=fish(bfs(babySharkPos[0],babySharkPos[1]))
        if res==False:
            return answer
        else:
            babySharkPos=res[0],res[1]
            answer+=res[2]
            graph[res[0]][res[1]]=0
            eatenFish+=1
        
        if eatenFish>=babySharkSize:
            babySharkSize+=1
            eatenFish=0

print(func())
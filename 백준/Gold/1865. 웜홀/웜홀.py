import sys
input=sys.stdin.readline
INF=10000

def func():
    for k in range(1,n+1): # 경유지
        for i in range(1,n+1):
            if k!=i:
                for j in range(1,n+1):
                    if k!=j:
                        route[i][j]=min(route[i][j],route[i][k]+route[k][j])
                        if route[i][i]<0:
                            return 'YES'
    return 'NO'

tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    route=[[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m): # 도로 정보 입력: 양방항, 최솟값으로 업데이트
        s,e,t=map(int,input().split())
        route[s][e]=min(route[s][e],t)
        route[e][s]=min(route[e][s],t)
    for _ in range(w): # 웜홀 정보 입력: 단방향, 최솟값으로 업데이트
        s,e,t=map(int,input().split())
        route[s][e]=min(route[s][e],(-1)*t) # 시간 정보는 *-1 처리 
    print(func())
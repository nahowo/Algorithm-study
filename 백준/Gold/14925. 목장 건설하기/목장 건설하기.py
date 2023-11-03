import sys
input=sys.stdin.readline

m,n=map(int,input().split())
land=[]
for _ in range(m):
    land.append(list(map(int,input().split())))
dp=[[0 for _ in range(n+1)] for _ in range(m+1)] # dp 테이블 정의
d=[(0,-1),(-1,-1),(-1,0)] # 이동할 방향
max_land=0

for i in range(1,m+1):
    for j in range(1,n+1):
        if land[i-1][j-1]==0: # 현재 위치가 들판인 경우
            tmp=[]
            for di,dj in d: # 위, 왼쪽 위, 왼쪽 확인
                ni,nj=i+di,j+dj

                tmp.append(dp[ni][nj])
            dp[i][j]=min(tmp)+1 # 세 방향 중 최소값+1을 현재 dp 위치에 저장
            max_land=max(max_land,dp[i][j])

        else: # 현재 위치에 나무나 바위가 있는 경우
            dp[i][j]=0
print(max_land)
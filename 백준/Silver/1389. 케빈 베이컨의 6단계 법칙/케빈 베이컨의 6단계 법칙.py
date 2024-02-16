import sys
input=sys.stdin.readline

# 1. 유저의 인맥 정보를 dp 테이블로 입력받는다. 
#     1. a-b 연결, b-a 연결
#     2. 본인-본인은 0으로 초기화
# 2. 3중 for문을 통해 테이블 업데이트
# 3. 각 행의 합 중에서 최솟값을 찾아 리턴

def func():
    n,m=map(int,input().split())
    INF=10**3
    dp=[[INF]*n for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        dp[a-1][b-1]=1
        dp[b-1][a-1]=1
    for i in range(0,n):
        dp[i][i]=0

    for k in range(n):
        for i in range(n):
            if i!=k:
                for j in range(n):
                    if i!=j and j!=k:
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

    bacon=[]
    for i in range(n):
        bacon.append([sum(dp[i]),i+1])
    return min(bacon)[1]
print(func())
import sys
input=sys.stdin.readline

def func():
    n=int(input())
    m=int(input())
    INF=10**7
    dp=[[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        dp[a][b]=min(dp[a][b],c)
    for i in range(1,n+1):
        dp[i][i]=0

    for k in range(1,n+1):
        for i in range(1,n+1):
            if i!=k:
                for j in range(1,n+1):
                    if i!=j and j!=k:
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

    for i in dp[1:]:
        for j in i[1:]:
            if j==INF:
                print(0,end=" ")
            else:
                print(j,end=" ")
        print("")
func()

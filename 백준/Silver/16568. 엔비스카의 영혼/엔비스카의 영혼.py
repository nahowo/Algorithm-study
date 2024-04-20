import sys
input=sys.stdin.readline

def func():
    n,a,b=map(int,input().split())
    if n<2:
        return n
    INF=10**7
    dp=[INF]*(n+1) # dp[i]: i번째 순서까지 도달하는 데 걸린 최소 시간
    dp[n]=0

    for i in range(n,-1,-1):
        tmp=dp[i]+1
        if i-1>=0:
            dp[i-1]=min(dp[i-1],tmp)
        if i-a-1>=0:
            dp[i-a-1]=min(dp[i-a-1],tmp)
        if i-b-1>=0:
            dp[i-b-1]=min(dp[i-b-1],tmp)
    return dp[0]
    
print(func())
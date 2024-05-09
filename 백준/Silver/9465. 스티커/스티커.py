import sys
input=sys.stdin.readline

def func():
    n=int(input())
    sticker=[]
    for _ in range(2):
        sticker.append([0,0]+list(map(int,input().split()))) # +2 패딩 처리
    dp=[[0]*(n+2) for _ in range(2)] # +2 패딩 처리

    for i in range(2,n+2):
        dp[0][i]=max(dp[1][i-2],dp[1][i-1])+sticker[0][i]
        dp[1][i]=max(dp[0][i-2],dp[0][i-1])+sticker[1][i]
    
    return max(dp[0][-1],dp[1][-1])

t=int(input())
for _ in range(t):
    print(func())
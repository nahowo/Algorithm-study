import sys
input=sys.stdin.readline

def func():
    n=int(input())
    s=list(map(int,input().split()))
    dpInc=[1]*(n) # 증가하는 부분 수열
    dpDec=[1]*(n) # 감소하는 부분 수열
    for i in range(n):
        for j in range(i):
            if s[i]>s[j]:
                dpInc[i]=max(dpInc[i],dpInc[j]+1)
    
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if s[i]>s[j]:
                dpDec[i]=max(dpDec[i],dpDec[j]+1)
    
    dp=[-1]*(n)
    for i in range(n):
        dp[i]+=dpInc[i]+dpDec[i]
    
    return max(dp)
print(func())
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(1,n):
    sum=1
    for j in range(i):
        if a[i]>a[j]:
            sum+=(dp[j]%998244353)
    dp[i]=sum%998244353
print(*dp)
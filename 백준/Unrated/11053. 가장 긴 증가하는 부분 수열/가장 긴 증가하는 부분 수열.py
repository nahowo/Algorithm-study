import sys
input=sys.stdin.readline
x=int(input())
arr=list(map(int,input().split()))
dp=[1]*x
for i in range(x):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
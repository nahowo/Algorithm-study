import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dp=[1]*(n+1)
arr=[]
for _ in range(m):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[1],x[0]))
for i in range(m):
    dp[arr[i][1]]=max(dp[arr[i][0]]+1,dp[arr[i][1]])
print(*dp[1:])
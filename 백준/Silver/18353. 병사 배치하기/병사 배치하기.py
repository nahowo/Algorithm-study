import sys
input=sys.stdin.readline
n=int(input())
soldiers=list(map(int,input().split()))
dp=[1 for _ in range(n)] #남아있는 병사 수
for i in range(n):
    for j in range(i):
        if soldiers[i]<soldiers[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
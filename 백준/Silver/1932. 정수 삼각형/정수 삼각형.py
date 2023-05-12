import sys
input=sys.stdin.readline
n=int(input())
dp=[list(map(int,input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j==0:
            dp[i][j]+=dp[i-1][0]
        elif j==len(dp[i])-1:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[-1]))
import sys
input=sys.stdin.readline

def func():
    s1=' '+input().rstrip()
    s2=' '+input().rstrip()
    n,m=len(s1),len(s2)
    dp=[[0]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            if s1[j]==s2[i]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[m-1][n-1]

print(func())
import sys
input=sys.stdin.readline

def func():
    a=[]
    n,m=map(int,input().split())
    table=[[0]*n]
    for _ in range(n):
        table.append([0]+list(map(int,input().split())))
    
    # dp 테이블 작성
    dp=[[0]*(n+1) for _ in range(n+1)] # 패딩 처리
    dp[1][1]=table[1][1]

    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j]=table[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
    
    # 누적합 계산
    for _ in range(m):
        x1,y1,x2,y2=map(int,input().split())
        answer=dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]
        print(answer)

func()
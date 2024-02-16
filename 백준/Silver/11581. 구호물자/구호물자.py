import sys
input=sys.stdin.readline

# 1. 교차로 정보 입력받기
#     1. 전부 False로 초기화
#     2. dp[i][a]=True
#     3. dp[i][i]도 False인 상태를 유지
# 2. 3중 for문을 통해 dp[i][k]와 dp[k][j]가 둘 다 True라면(연결되어 있다면) dp[i][j]도 True
# 3. dp[i][i]=True인 것이 있으면 CYCLE, 없으면 NO CYCLE
#     1. 사이클이 생기더라도 해당 사이클이 1과 연결되어 있지 않다면 사이클에 들어갈 수 없으므로 dp[1][i]=True인지 확인

def func():
    n=int(input())
    dp=[[False]*n for _ in range(n)]
    for i in range(n-1):
        m=int(input())
        arr=list(map(int,input().split()))
        for j in range(m):
            dp[i][arr[j]-1]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j]=True
    
    for i in range(n):
        if dp[i][i] and dp[0][i]:
            return "CYCLE"
    return "NO CYCLE"

print(func())
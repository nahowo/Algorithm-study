import sys
input=sys.stdin.readline

# 1. 회원의 인맥 정보 입력
#     1. dp 테이블은 전부 n-1로 초기화(n명의 회원이 있을 때 가질 수 있는 점수의 최대값)
#     2. dp[a][b]=1, dp[b][a]=1
#     3. dp[i][i]=0
# 2. 3중 for문을 이용해 인맥 정보 테이블 업데이트
# 3. 테이블의 i행별 최대값(점수)과 회원번호를 저장, 최저 점수와 후보 수를 출력하고 회장 후보를 오름차순 출력

def func():
    n=int(input())
    dp=[[n-1]*n for _ in range(n)] # 최대 점수
    while True:
        a,b=map(int,input().split())
        if a==-1 and b==-1:
            break
        dp[a-1][b-1]=1
        dp[b-1][a-1]=1
    for i in range(n):
        dp[i][i]=0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
    
    member=[]
    for i in range(n):
        member.append(max(dp[i]))
    min_point=min(member)
    candidate=[]
    for i in range(n):
        if member[i]==min_point:
            candidate.append(i+1)
    candidate.sort()
    print(min_point,len(candidate))
    print(*candidate)
    
func()
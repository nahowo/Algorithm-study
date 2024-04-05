import sys
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    m=10**6*2
    ice=[0]*(m+2) # 패딩 추가
    maxIce=0

    for _ in range(n):
        g,x=map(int,input().split())
        ice[x+1]=g
    
    iceSum=[0] # 누적합 계산
    for i in range(1,m+2):
        iceSum.append(iceSum[i-1]+ice[i])

    if k*2+1>=m: # 이동 가능한 공간이 10^6을 넘어가는 경우: 모든 얼음을 가질 수 있음
        return sum(ice)

    for i in range(m-(k*2-1)): # 얼음들의 합 중 최댓값 계산
        maxIce=max(maxIce, iceSum[i+(k*2+1)] - iceSum[i])
    return maxIce

print(func())
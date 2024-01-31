import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    gate=[]
    for _ in range(n): # 출구/입구만 입력받기
        tmp=list(map(int,input().split()))
        gate.append(tmp[1])
        gate.append(tmp[tmp[0]])
    
    gate.sort() # len(gate) == 2*n
    return gate[n-1] # 가능한 지점 중 번호가 가장 작은 곳
    
print(func())
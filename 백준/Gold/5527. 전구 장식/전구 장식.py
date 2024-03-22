import sys
input=sys.stdin.readline

def func():
    n=int(input())
    bulb=list(map(int,input().split()))
    pattern=[]
    
    cnt=1
    for i in range(1,n):
        if bulb[i-1]!=bulb[i]:
            cnt+=1
        else:
            pattern.append(cnt)
            cnt=1
    pattern.append(cnt)

    if len(pattern)<3:
        return n
    
    sumP=[0]
    for i in range(len(pattern)):
        sumP.append(pattern[i]+sumP[i])
    
    # 누적합 계산
    maxLen=0
    for i in range(3,len(sumP)):
        maxLen=max(maxLen,sumP[i]-sumP[i-3])
    return maxLen

print(func())
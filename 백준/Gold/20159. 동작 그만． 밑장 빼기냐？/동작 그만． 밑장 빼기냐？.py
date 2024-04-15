import sys
input=sys.stdin.readline

def func():
    n=int(input())
    card=list(map(int,input().split()))
    odd=[0] # 홀수 누적합
    even=[0] # 짝수 누적합

    for i in range(n): # 누적합 계산
        if i%2==0:
            odd.append(card[i]+odd[i])
            even.append(even[-1])
        else:
            even.append(card[i]+even[i])
            odd.append(odd[-1])

    maxCard=max(odd[-1],even[-1])

    for i in range(1,n+1):
        if i%2==1:
            tmp=odd[i-1]+even[n]-even[i]
        else:
            tmp=odd[i-1]+even[n-1]-even[i-1]
        maxCard=max(maxCard,tmp)
    return maxCard
    
print(func())
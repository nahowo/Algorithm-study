import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    t=list(map(int,input().split()))
    if m==0:
        return 0

    money=t[0]
    profit=[0]*n
    profit[0]=t[0]
    for i in range(1,m):
        profit[i]=profit[i-1]+t[i]
        money=max(money,profit[i])
    for i in range(m,n):
        profit[i]=profit[i-1]+t[i]-t[i-m]
        money=max(money,profit[i])
    return money

print(func())
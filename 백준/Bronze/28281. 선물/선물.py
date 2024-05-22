import sys
input=sys.stdin.readline

def func():
    n,x=map(int,input().split())
    socks=list(map(int,input().split()))
    m=float("inf")

    for i in range(n-1):
        tmp=socks[i]+socks[i+1]
        m=min(m,tmp)
    return m*x

print(func())
import sys
input=sys.stdin.readline
MOD=1000000007

def calc(n,x):
    if x==1:
        return n
    v=calc(n,x//2)
    if x%2==0:
        return v*v%MOD
    else:
        return (v**2)*n%MOD

def func():
    m=int(input())
    cnt=0
    for _ in range(m):
        n,s=map(int,input().split())
        tmp=calc(n,MOD-2)
        cnt=(cnt+(tmp*s%MOD))%MOD
    return cnt

print(func())
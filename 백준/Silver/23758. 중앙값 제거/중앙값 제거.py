import sys
from math import log2
input=sys.stdin.readline

def func():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    cnt=0
    
    if n%2:
        k=(n//2)+1
    else:
        k=n//2

    for i in range(k):
        tmp=a[i]
        cnt+=int(log2(tmp))
    return cnt+1

print(func())
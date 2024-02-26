import sys
from collections import deque
input=sys.stdin.readline

def func():
    m,n,x,y=map(int,input().split())
    k=x
    while k<=m*n:
        if (k-x)%m==0 and (k-y)%n==0:
            return k
        k+=m
    return -1

t=int(input())
for _ in range(t):    
    print(func())
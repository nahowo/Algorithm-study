import sys
input=sys.stdin.readline

def func():
    n,c=map(int,input().split())
    time=[0]*c
    for _ in range(n):
        tmp=int(input())
        if tmp==1:
            return c
        time[tmp-1::tmp]=[1]*(c//tmp)
    return sum(time)
print(func())
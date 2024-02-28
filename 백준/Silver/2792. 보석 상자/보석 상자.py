import sys
input=sys.stdin.readline
    
def func():
    n,m=map(int,input().split())
    gem=[]
    for _ in range(m):
        gem.append(int(input()))
    s=1
    e=max(gem)
    while s<=e:
        m=(s+e)//2
        tmp=0
        for i in gem:
            if i%m==0:
                tmp+=i//m
            else:
                tmp+=i//m+1
        if tmp>n:
            s=m+1
        else:
            e=m-1
    return s


print(func())
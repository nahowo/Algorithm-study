import sys
input=sys.stdin.readline
    
def func():
    _=input()
    a,b,c,d=map(int,input().split())
    if d==0:
        return a*b*c
    a,b,c,=sorted((a,b,c))
    cake=sum([a,b,c])-d
    tmp=min(cake//3,a)
    ta=tmp
    cake-=tmp
    tmp=min(cake//2,b)
    return ta*tmp*(cake-tmp)

t=int(input())
for _ in range(t):
    print(func())
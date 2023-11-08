import sys
input=sys.stdin.readline

t=int(input())
def func():
    n,k=map(int,input().split())
    s,e=0,5000
    while s<e:
        m=(s+e)//2
        if k*(m+1)*m<n*2:
            s=m+1
        else:
            e=m
    sum=s*(s+1)//2
    if s%2!=0:
        tmp=k*(s//2+1)
        tmp+=(n-1)-sum*k
        pos='R'
    else:
        tmp=-k*(s//2)
        tmp-=(n-1)-sum*k
        pos='L'
    print(str(tmp),pos)
    return

for _ in range(t):
    func()
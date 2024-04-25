import sys
input=sys.stdin.readline

def mlt(a,b):
    n=len(a)
    arr=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            e=0
            for k in range(n):
                e+=a[i][k]*b[k][j]
            arr[i][j]=e%1000
    return arr

def sqr(a,b):
    if b==1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j]%=1000
        return a
    tmp=sqr(a,b//2)
    if b%2:
        return mlt(mlt(tmp,tmp),a)
    else:
        return mlt(tmp,tmp)

n,b=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
answer=sqr(a,b)
for i in answer:
    print(*i)
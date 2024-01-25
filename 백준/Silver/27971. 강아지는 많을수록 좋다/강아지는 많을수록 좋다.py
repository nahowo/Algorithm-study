import sys
input=sys.stdin.readline

def func():
    n,m,a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    dog=[0]*(n+1)
    dog[0]=0

    for _ in range(m):
        op,cl=map(int,input().split())
        for i in range(op,cl+1):
            dog[i]=-1

    for i in range(1,n+1):
        if dog[i]==-1:
            continue
        if i<a:
            dog[i]=-1
        elif i<b:
            if dog[i-a]==-1:
                dog[i]=-1
            else:
                dog[i]=dog[i-a]+1
    
        elif dog[i-a]==-1 and dog[i-b]==-1:
            dog[i]=-1
        elif dog[i-a]==-1:
            dog[i]=dog[i-b]+1
        elif dog[i-b]==-1:
            dog[i]=dog[i-a]+1
        else:
            dog[i]=min(dog[i-a],dog[i-b])+1
    return dog[n]

print(func())
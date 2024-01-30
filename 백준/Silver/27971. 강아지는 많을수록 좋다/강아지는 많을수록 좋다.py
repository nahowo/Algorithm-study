import sys
input=sys.stdin.readline

def func():
    n,m,a,b=map(int,input().split())
    dog=[0]+[-1]*n

    for _ in range(m):
        op,cl=map(int,input().split())
        dog[op:cl+1]=[-2]*(cl-op+1)

    for i in range(min(a,b),n+1):
        if dog[i]!=-2:
            if dog[i-a]<0 or dog[i-b]<0:
                if dog[i-a]>=0:
                    dog[i]=dog[i-a]+1
                if dog[i-b]>=0:
                    dog[i]=dog[i-b]+1
            else:
                dog[i]=min(dog[i-a],dog[i-b])+1

    return dog[-1] if dog[-1]>0 else -1

print(func())
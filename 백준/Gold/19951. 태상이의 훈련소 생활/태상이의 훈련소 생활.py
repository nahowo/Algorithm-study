import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    dirt=[0]+list(map(int,input().split()))
    dig=[0]*(n+2)

    for _ in range(m):
        a,b,c=map(int,input().split())
        dig[a]+=c
        dig[b+1]-=c
    
    dirt[0]+=dig[0]
    for i in range(1,n+1):
        dig[i]+=dig[i-1]
        dirt[i]+=dig[i]
    return dirt[1:]

print(*func())
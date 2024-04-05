import sys
input=sys.stdin.readline

def func():
    n=int(input())
    blop=list(map(int,input().split()))
    maxL=max(blop)

    for i in range(1,n-1):
        maxL=max(maxL,blop[i]+min(blop[i-1],blop[i+1]))
    
    return maxL

print(func())
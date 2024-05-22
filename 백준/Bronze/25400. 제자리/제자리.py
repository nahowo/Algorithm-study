import sys
input=sys.stdin.readline

def func():
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    i=0
    k=1
    while i<n:
        if a[i]!=k:
            cnt+=1
        else:
            k+=1
        if i==n:
            break
        i+=1
    return cnt
print(func())
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
N=list(map(int,input().split()))
M=[]
sum=0
for i in range(n):
    tmp=N[i]
    sum+=tmp
    N[i]=sum
for _ in range(m):
    M.append(int(input()))
for i in M:
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if N[mid]<i:
            start=mid+1
        elif N[mid]>i:
            end=mid-1
        else:
            end=mid
            break
    print(end+1)
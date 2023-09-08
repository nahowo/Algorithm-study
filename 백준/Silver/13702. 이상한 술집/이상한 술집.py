import sys
input=sys.stdin.readline
n,k=map(int,input().split())
drink=[int(input()) for _ in range(n)]
start=1
end=max(drink)
while start<=end:
    mid=(start+end)//2
    tmp=sum(i//mid for i in drink)
    if tmp>=k:
        answer=mid
        start=mid+1
    else:
        end=mid-1
print(answer)
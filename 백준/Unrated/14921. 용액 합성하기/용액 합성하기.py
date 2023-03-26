import sys
input=sys.stdin.readline
n=int(input())
sol=list(map(int,input().split()))
l=0
r=n-1
ans=sol[r]+sol[l]
while l<r:
    min_=sol[l]+sol[r]
    if abs(min_)<abs(ans):
        ans=min_
    if min_==0:
        break
    elif min_>0:
        r-=1
    else:
        l+=1
print(ans)
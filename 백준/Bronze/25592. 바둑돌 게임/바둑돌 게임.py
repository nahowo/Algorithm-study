import sys
input=sys.stdin.readline

n=int(input())
sum=0
i=0
while sum<=n:
    i+=1
    sum+=i
if i%2==1:
    print(sum-n)
elif i%2==0:
    if sum==n:
        print(1)
    else:
        print(0)
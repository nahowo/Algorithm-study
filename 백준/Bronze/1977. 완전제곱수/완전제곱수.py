import sys
input=sys.stdin.readline
m=int(input())
n=int(input())
sum_=0
min_=0
for i in range(int(n**(1/2))+1,int(m**(1/2))-1,-1):
    if i**2>=m and i**2<=n:
        sum_+=i**2
        min_=i**2
if sum_==0:
    print(-1)
else:
    print(sum_)
    print(min_)
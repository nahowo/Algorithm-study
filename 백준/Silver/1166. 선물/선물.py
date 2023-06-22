import sys
input=sys.stdin.readline
n,l,w,h=map(int,input().split())
high=min(l,w,h)
low=0
for _ in range(10000):
    mid=(high+low)/2
    tmp=(l//mid)*(w//mid)*(h//mid)
    if tmp>=n:
        low=mid
    else:
        high=mid
print("%.15f" %(high))
import sys
input=sys.stdin.readline

n=int(input())
a=int(input())
angle=0

for i in range(n):
    tmp=int(input())
    if tmp>=a:
        angle+=min(tmp-a,a+360-tmp)
    else:
        angle+=min(a-tmp,tmp+360-a)
    a=tmp
print(angle)
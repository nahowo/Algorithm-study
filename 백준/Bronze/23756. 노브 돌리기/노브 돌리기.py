import sys
input=sys.stdin.readline

n=int(input())
a=int(input())
angle=0

for i in range(n):
    tmp=int(input())
    a=abs(a-tmp)
    angle+=min(a,360-a)
    a=tmp
print(angle)
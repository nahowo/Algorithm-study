import sys
input=sys.stdin.readline
n,m=map(int,input().split())
j=int(input())
apple=[int(input()) for _ in range(j)]
current=m
distance=0
for i in apple:
    next=i
    if current>=i and i>current-m:
        continue
    if current<next:
        moved=next-current
    else:
        moved=next-(current-m+1)
    current+=moved
    distance+=abs(moved)
print(distance)
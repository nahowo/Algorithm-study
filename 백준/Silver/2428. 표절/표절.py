import sys
from collections import deque
n=int(input())
solution=list(map(int,input().split()))
solution.sort()
answer=0
for i in range(n-1):
    s=i+1
    e=n-1
    tmp=0
    while s<=e:
        m=(s+e)//2
        if solution[i]>=0.9*solution[m]:
            tmp=m
            s=m+1
        else:
            e=m-1
    if tmp!=0:
        answer+=tmp-i
print(answer)
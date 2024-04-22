import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
train=[deque([0]*20) for _ in range(n)]
for i in range(m):
    tmp=list(map(int,input().split()))
    command=tmp[0]
    i=tmp[1]-1
    if command==1 or command==2:
        x=tmp[2]-1
    if command==1:
        train[i][x]=1
    elif command==2:
        train[i][x]=0
    elif command==3:
        train[i].appendleft(0)
        train[i].pop()
    elif command==4:
        train[i].append(0)
        train[i].popleft()
passed=[]
for i in train:
    if i not in passed:
        passed.append(i)
print(len(passed))
from collections import deque
n,m=map(int,input().split())
if n==0:
    print(0)
    exit()
boxes=deque(map(int,input().split()))
tmp=0
minbox=0
for i in range(n):
    if tmp+boxes[i]>m:
        tmp=0
        minbox+=1
    tmp+=boxes[i]
print(minbox+1)
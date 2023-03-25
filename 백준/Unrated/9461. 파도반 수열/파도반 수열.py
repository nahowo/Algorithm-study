import sys
input=sys.stdin.readline
t=int(input())
tcs=[]
for _ in range(t):
    tcs.append(int(input()))
maxt=max(tcs)
d=[0]*101
d[1]=d[2]=d[3]=1
for i in range(4,maxt+1):
    d[i]=d[i-3]+d[i-2]
for i in tcs:
    print(d[i])
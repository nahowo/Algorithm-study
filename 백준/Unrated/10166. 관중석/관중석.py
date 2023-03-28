import sys
input=sys.stdin.readline
d1,d2=map(int,input().split())
seat=[0]*360
seat[0]=1
for i in range(d1,d2+1):
    for j in range(1,i):
        tmp=360//i
        seat[tmp*j]=1
print(sum(seat))
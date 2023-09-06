import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ring=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    tmpcnt=tmp.count(1)
    ring.append([tmp,tmpcnt])
ring.sort(key=lambda x:x[1])
def func():
    global n,m
    for i in range(1,n):
        for j in range(m):
            if ring[i-1][0][j]==1 and ring[i][0][j]==0:
                return "NO"
    return "YES"
print(func())
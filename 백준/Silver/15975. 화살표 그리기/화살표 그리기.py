import sys
input=sys.stdin.readline
n=int(input())
dots=[[] for _ in range(n+1)]
lp=0
for _ in range(n):
    x,y=map(int,input().split())
    dots[y].append(x)
for i in range(1,n+1):
    if len(dots[i])>=2:
        dots[i].sort()
        lp+=dots[i][1]-dots[i][0]
        for j in range(1,len(dots[i])-1):
            lp+=min((dots[i][j]-dots[i][j-1]),(dots[i][j+1]-dots[i][j]))
        lp+=dots[i][-1]-dots[i][-2]
print(lp)
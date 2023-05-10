import sys
input=sys.stdin.readline
n=int(input())
a,b=map(int,input().split())
dots=[tuple(map(int,input().split())) for _ in range(n)]
dots=set(dots)
d=[[a,0],[a,b],[0,b]]
def func(i):
    for di in d:
        nx=i[0]+di[0]
        ny=i[1]+di[1]
        if (nx,ny) not in dots:
            return False
    return True
answer=0
for dot in dots:
    if func(dot)==True:
        answer+=1
print(answer)
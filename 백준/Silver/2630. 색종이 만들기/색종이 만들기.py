import sys
input=sys.stdin.readline

def count(n,s,e):
    cnt=0
    for i in range(s,s+n):
        for j in range(e,e+n):
            if paper[i][j]==1:
                cnt+=1
    return cnt

def func(n,x,y):
    global white,blue
    total=count(n,x,y)
    if total==n**2:
        blue+=1
    elif total==0:
        white+=1
    else:
        func(n//2,x,y)
        func(n//2,x+n//2,y)
        func(n//2,x,y+n//2)
        func(n//2,x+n//2,y+n//2)
    return

n=int(input())
paper=[]
for _ in range(n):
    paper.append(list(map(int,input().split())))
blue=white=0

func(n,0,0)
print(white)
print(blue)
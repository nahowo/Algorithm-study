import sys
input=sys.stdin.readline

def func(sx,sy,ex,ey):
    for i in range(sx,ex+1):
        for j in range(sy,ey+1):
            if i==1 and j==1:
                continue
            else:
                m[i][j]=(m[i-1][j]+m[i][j-1])%1000007

w,h=map(int,input().split())
x,y=map(int,input().split())
m=[[0]*(h+1) for _ in range(w+1)]
m[1][1]=1
func(1,1,x,y)
func(x,y,w,h)

print(m[w][h])
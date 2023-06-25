import sys
input=sys.stdin.readline
a,b,c,d,e,f=map(int,input().split())
def func():
    for i in range(-999,1000):
        for j in range(-999,1000):
            if a*i+b*j==c and d*i+e*j==f:
                return i,j
x,y=func()
print(x,y)
import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

def func(x,y):
    if y==1:
        return x%c
    if y%2==0:
        return (func(x,y//2)**2)%c
    else:
        return ((func(x,y//2)**2)*x)%c

print(func(a,b))
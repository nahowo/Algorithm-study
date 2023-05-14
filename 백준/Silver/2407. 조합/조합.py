import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def fact(a):
    f=1
    for i in range(2,a+1):
        f*=i
    return f
print(fact(n)//(fact(n-m)*fact(m)))
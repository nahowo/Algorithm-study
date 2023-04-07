import sys
input=sys.stdin.readline
a,b=map(int,input().split())
def gcd(A,B):
    while B>0:
        A,B=B,A%B
    return A
gcd_=gcd(a,b)
print(a*b//gcd_)
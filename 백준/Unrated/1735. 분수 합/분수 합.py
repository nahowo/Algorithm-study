import sys
input=sys.stdin.readline
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
n1,d1=map(int,input().split())
n2,d2=map(int,input().split())
GCD=gcd(d1,d2)
LCM=d1*d2//GCD
N=n1*LCM//d1+n2*LCM//d2
D=LCM
GCD2=gcd(N,D)
fr=[N//GCD2,D//GCD2]
print(*fr)
import sys
input=sys.stdin.readline

def func():
    n,k,a,b=map(int,input().split())
    pot=[k]*(n//a)
    day=1
    while True:
        for i in range(n//a):
            pot[i]+=b
            for j in range(n//a):
                pot[j]-=1
                if pot[j]==0:
                    return day
            day+=1

print(func())
import sys
input=sys.stdin.readline

def func():
    n,c=map(int,input().split())
    fire=[0]*(2000001)
    for _ in range(n):
        tmp=int(input())
        k=tmp
        while True:
            if k<=c:
                fire[k]=1
                k+=tmp
            else:
                break
    return sum(fire)

print(func())
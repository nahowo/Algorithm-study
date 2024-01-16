import sys
input=sys.stdin.readline

def func():
    n,m,k=map(int,input().split())
    a,b,c,d=n,m,0,0
    cnt=0
    if k==1 and m==1 and n>m:
        return -1
    
    while True:
        # 창의인재관 -> 융합인재관
        x=min(k*m,a)
        y=m
        a-=x
        b-=y
        c+=x
        d+=y
        cnt+=1
        if c==n:
            break
        
        # 융합인재관 -> 창의인재관
        z=1
        w=m
        a+=z
        b+=w
        c-=z
        d-=w
        cnt+=1
    return cnt

t=int(input())
for _ in range(t):
    print(func())
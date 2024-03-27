import sys
input=sys.stdin.readline

a,b=map(int,input().split())
flag=False

def func(i,cnt):
    global flag
    if i==b:
        print(cnt)
        flag=True
        return
    for ni in [i*2,i*10+1]:
        if ni<=10**9:
            func(ni,cnt+1)

func(a,1)
if not flag:
    print(-1)
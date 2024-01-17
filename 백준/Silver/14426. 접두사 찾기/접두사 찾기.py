import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    s=set()
    cnt=0
    for _ in range(n):
        tmp=input().rstrip()
        for i in range(1,len(tmp)+1):
            s.add(tmp[:i])
    for i in range(m):
        check=input().rstrip()
        if check in s:
            cnt+=1
    return cnt

print(func())
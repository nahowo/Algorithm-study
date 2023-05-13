import sys
input=sys.stdin.readline
n,k=map(int,input().split())
s=set([i for i in range(2,n+1)])
def func():
    cnt=0
    for i in range(2,n+1):
        for j in range(1,n//i+1):
            if i*j in s:
                s.remove(i*j)
                cnt+=1
                if cnt==k:
                    return i*j
print(func())
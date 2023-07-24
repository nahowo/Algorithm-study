import sys
input=sys.stdin.readline
n=int(input())
ask_to=[0]
for _ in range(n):
    ask_to.append(int(input()))
m=0
def func(s):
    cnt=0
    visited=[False]*(n+1)
    visited[s]=True
    next=ask_to[s]
    while True:
        if visited[next]==False:
            visited[next]=True
            cnt+=1
        else:
            cnt+=1
            return cnt
        next=ask_to[next]
for i in range(1,n+1):
    tmp=func(i)
    if tmp>m:
        answer=i
        m=tmp
print(answer)
import sys
from collections import deque
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    if n==k:
        print(0)
        print(1)
        return
    
    q=deque()
    q.append(n)
    maxnum=10**5+1
    visited=[0]*(maxnum+1)
    answer=0
    cnt=0

    while q:
        x=q.popleft()
        if x==k:
            answer=visited[x]
            cnt+=1
        for nx in [x+1,x-1,x*2]:
            if 0<=nx<=maxnum:
                if visited[nx]==0 or visited[nx]==visited[x]+1:
                    visited[nx]=visited[x]+1
                    q.append(nx)
    print(answer)
    print(cnt)
    return

func()
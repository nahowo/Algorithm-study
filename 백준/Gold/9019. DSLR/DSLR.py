import sys
from collections import deque
input=sys.stdin.readline

def func():
    a,b=map(int,input().split())
    c=['D','S','L','R']
    q=deque([[a,'']])
    visited=[False]*10000

    while q:
        n,cmd=q.popleft()
        if n==b:
            return cmd
        arr=[(n*2)%10000, (n-1)%10000, (n*10+(n//1000))%10000, (n//10)+(n%10)*1000]
        for i in range(4):
            if not visited[arr[i]]:
                q.append([arr[i],cmd+c[i]])
                visited[arr[i]]=True

t=int(input())
for _ in range(t):
    print(func())
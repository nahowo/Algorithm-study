import sys
from collections import deque
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    if n==k:
        return 0
    maxi=10**5
    graph=[maxi]*(maxi+1)
    graph[n]=0
    q=deque([n])

    while q:
        x=q.popleft()
        for nx in [x+1, x-1]:
            if 0<=nx<=maxi and graph[nx]>graph[x]+1:
                graph[nx]=graph[x]+1
                q.append(nx)
        for nx in [2*x]:
            if 0<=nx<=maxi and graph[nx]>graph[x]:
                graph[nx]=graph[x]
                q.append(nx)
    return graph[k]

print(func())
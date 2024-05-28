import sys
from collections import deque
input=sys.stdin.readline

def jump():
    n=int(input())
    stone=[0]+list(map(int,input().split()))
    a,b=map(int,input().split())
    cnt=[-1]*(n+1)
    cnt[a]=0
    q=deque()
    q.append(a)

    while q:
        x=q.popleft()
        for nx in range(x,n+1,stone[x]):
            if cnt[nx]==-1: # 방문하지 않은 경우
                q.append(nx)
                cnt[nx]=cnt[x]+1
                if nx==b:
                    return cnt[b]
        for nx in range(x,0,stone[x]*(-1)):
            if cnt[nx]==-1: # 방문하지 않은 경우
                q.append(nx)
                cnt[nx]=cnt[x]+1
                if nx==b:
                    return cnt[b]
    return -1

print(jump())
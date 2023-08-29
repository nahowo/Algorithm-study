import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[int(input()) for _ in range(n)]
q=[int(input()) for _ in range(m)]
a.sort()
d=dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]]=i
for i in q:
    try:
        print(d[i])
    except:
        print(-1)
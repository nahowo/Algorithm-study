import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
tree=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    tree[b].append(a)
x=int(input())
cnt=0
q=deque([x])
visited={x}
while q:
    x=q.pop()
    for i in tree[x]:
        if i not in visited:
            q.append(i)
            visited.add(i)
            cnt+=1
print(cnt)
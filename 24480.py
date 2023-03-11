from collections import deque
import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
visited=[0]*(n+1)
def dfs(R):
    s=deque([R])
    count=1
    while s:
        x=s.pop()
        if visited[x]==0:
            visited[x]=count
            count+=1
            for i in graph[x]:
                if visited[i]==0:
                    s.append(i)
    return 0
dfs(r)
for i in visited[1:]:
    print(i)
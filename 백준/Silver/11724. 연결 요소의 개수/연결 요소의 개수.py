import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
compo=set()
connected=0
def bfs(a):
    # if graph[a][0] in compo:
    #     return 0
    q=deque([a])
    compo.add(a)
    while q:
        x=q.popleft()
        for i in graph[x]:
            if i not in compo: #x와 연결된 노드를 방문하지 않았을 때
                q.append(i)
                compo.add(i) #방문 완료
    return 1
for i in range(1,n+1):
    if i not in compo:
        if not graph[i]:
            compo.add(i)
        else:
            bfs(i)
        connected+=1
print(connected)
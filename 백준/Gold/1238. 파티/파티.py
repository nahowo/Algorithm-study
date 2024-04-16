import sys
import heapq
input=sys.stdin.readline
INF=1e10

def dijkstra(s, edge):
    dist=[INF] * (n+1)
    q=[]
    heapq.heappush(q,(s,0))
    while q:
        w,d=heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt,c in edge[w]:
            if dist[nxt] > d + c:
                dist[nxt]=d+c
                heapq.heappush(q,(nxt,d+c))
    return dist

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))
node2x=dijkstra(x,reverse_graph)
x2node=dijkstra(x,graph)

print(max([x2node[i] + node2x[i] for i in range(1,n+1) if i != x]))
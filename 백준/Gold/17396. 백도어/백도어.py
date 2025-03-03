import sys
import heapq
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 10 + 1

def solution():
    n, m = map(int, input().split())
    visible = list(map(int, input().split()))
    visible[n - 1] = 0
    graph = [[] for _ in range(n)]
    dist = [INF] * n
    dist[0] = 0
    for _ in range(m):
        a, b, t = map(int, input().split())
        if not visible[a]:
            graph[a].append([b, t])
        if not visible[b]:
            graph[b].append([a, t])

    q = [[0, 0]]
    while q:
        d, x = heapq.heappop(q)
        if d > dist[x]:
            continue
        for nx, nd in graph[x]:
            if d + nd < dist[nx]:
                dist[nx] = d + nd
                heapq.heappush(q, [dist[nx], nx])

    if dist[n - 1] == INF:
        return -1
    return dist[n - 1]
    
print(solution())
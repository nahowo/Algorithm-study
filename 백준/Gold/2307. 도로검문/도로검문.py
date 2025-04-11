import sys, heapq
from collections import deque
input = sys.stdin.readline
INF = 10 ** 8

def dijkstra(n, graph, ignoreA, ignoreB):
    dist = [INF] * (n + 1)
    dist[1] = 0
    prev = [[] for i in range(n + 1)]

    q = [[0, 1]]
    while q:
        d, x = heapq.heappop(q)
        if d > dist[x]:
            continue
        for nx, nd in graph[x]:
            if (x == ignoreA and nx == ignoreB) or (x == ignoreB and nx == ignoreA):
                continue
            if d + nd < dist[nx]:
                dist[nx] = d + nd
                prev[nx] = [x]
                heapq.heappush(q, [dist[nx], nx])
            elif d + nd == dist[nx]:
                prev[nx].append(x)

    if ignoreA == -1 and ignoreB == -1: # 첫 번째 정상 다익스트라만 BFS로 최단경로(실제 경로) 계산
        q = deque([n])
        visited = [False] * (n + 1)
        visited[n] = True
        while q:
            x = q.popleft()
            for nx in prev[x]:
                toVisit.add((x, nx))
                q.append(nx)

    if dist[n] >= INF:
        return -1
    return dist[n]

def solution():
    global toVisit
    n, m = map(int, input().split())
    route = []
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        route.append((a, b))
        graph[a].append([b, t])
        graph[b].append([a, t])

    toVisit = set() # 검문해야 하는 모든 간선(모든 최단 경로에 속하는 모든 간선)
    originalT = dijkstra(n, graph, -1, -1)
    result = -1

    for a, b in toVisit:
        tmpT = dijkstra(n, graph, a, b)
        if tmpT == -1:
            return -1
        result = max(result, tmpT - originalT)
    return result

print(solution())
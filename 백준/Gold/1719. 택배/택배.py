import sys, heapq
input = sys.stdin.readline
INF = 10 ** 7

def dijkstra(sx):
    dist = [INF] * (n + 1)
    dist[sx] = 0
    q = [[0, sx]]
    while q:
        tdist, x = heapq.heappop(q)
        if dist[x] < tdist:
            continue
        for nx, nc in graph[x]:
            if dist[nx] > tdist + nc:
                dist[nx] = tdist + nc
                heapq.heappush(q, [dist[nx], nx])
                result[nx][sx] = x

def solution():
    global n, result, graph
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    result = [['-'] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    for i in range(1, n + 1):
        dijkstra(i)
    
    for i in range(1, n + 1):
        print(' '.join(map(str, result[i][1:])))

solution()
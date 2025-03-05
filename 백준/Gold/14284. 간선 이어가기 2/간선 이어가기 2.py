import sys, heapq
input = sys.stdin.readline
INF = 10 ** 7 + 1

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    s, t = map(int, input().split())

    dist = [INF] * (n + 1)
    dist[s] = 0
    q = [[0, s]]

    while q:
        d, x = heapq.heappop(q)
        if x == t:
            return d
        if dist[x] < d:
            continue
        for nx, nd in graph[x]:
            if dist[nx] > d + nd:
                dist[nx] = d + nd
                heapq.heappush(q, [dist[nx], nx])

print(solution())
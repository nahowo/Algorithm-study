import sys, heapq
input = sys.stdin.readline
INF = 10 ** 3 + 1

def solution():
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)

    dist = [INF] * (n + 1)
    dist[a] = 0
    q = [[dist[a], a]]
    while q:
        d, x = heapq.heappop(q)
        if dist[x] < d:
            continue
        if x == b:
            return dist[x]
        for nx in graph[x]:
            if dist[nx] > d + 1:
                dist[nx] = d + 1
                heapq.heappush(q, [d + 1, nx])

    return -1

print(solution())
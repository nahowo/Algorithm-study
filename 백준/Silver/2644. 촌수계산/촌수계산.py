import sys, heapq
input = sys.stdin.readline
INF = 10 ** 2

def solution():
    n = int(input())
    s, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    dist = [INF] * (n + 1)
    dist[s] = 0
    q = [[0, s]]
    while q:
        d, x = heapq.heappop(q)
        if x == e:
            return d
        if dist[x] < d:
            continue
        for nx in graph[x]:
            if dist[nx] > d + 1:
                dist[nx] = d + 1
                heapq.heappush(q, [dist[nx], nx])
    return -1

print(solution())
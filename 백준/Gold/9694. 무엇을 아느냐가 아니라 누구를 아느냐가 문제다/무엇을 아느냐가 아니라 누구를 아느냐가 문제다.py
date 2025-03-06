import sys, heapq
input = sys.stdin.readline
INF = 10 ** 2    

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(m)]
    for _ in range(n):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    parent = [i for i in range(m)]
    dist = [INF] * m
    dist[0] = 0
    q = [[0, 0]]
    while q:
        d, x = heapq.heappop(q)
        if x == m - 1:
            dist[x] = d
            break
        if dist[x] < d:
            continue
        for nx, nd in graph[x]:
            if dist[nx] > d + nd:
                dist[nx] = d + nd
                heapq.heappush(q, [dist[nx], nx])
                parent[nx] = x
    route = []
    nxt = m - 1
    cnt = 0
    while cnt <= m:
        route.append(nxt)
        if nxt == 0:
            break
        cnt += 1
        nxt = parent[nxt]
    if nxt != 0:
        return [-1]
    return route[::-1]

t = int(input())
for i in range(1, t + 1):
    print("Case #" + str(i) + ": " + ' '.join(map(str, solution())))
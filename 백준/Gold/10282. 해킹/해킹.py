import sys, heapq
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 8

def solution():
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    time = [INF] * (n + 1)
    time[c] = 0
    q = [[0, c]]

    while q:
        td, x = heapq.heappop(q)
        if time[x] < td:
            continue
        for nx, nd in graph[x]:
            if time[nx] > td + nd:
                time[nx] = td + nd
                heapq.heappush(q, [time[nx], nx])

    cnt = 0
    maxTime = 0
    for i in range(1, n + 1):
        if time[i] != INF:
            cnt += 1
            maxTime = max(maxTime, time[i])
    return cnt, maxTime

t = int(input())
for _ in range(t):
    print(*solution())
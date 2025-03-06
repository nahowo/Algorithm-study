import sys, heapq
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 10 ** 4

def solution():
    n, m, a, b, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        n1, n2, c1 = map(int, input().split())
        graph[n1].append([n2, c1])
        graph[n2].append([n1, c1])

    dist = [[INF, INF] for _ in range(n + 1)] # 한 골목의 최대 요금, 전체 경로 요금
    dist[a] = [0, 0]
    q = [[0, 0, a]]
    while q:
        maxC, totalC, x = heapq.heappop(q)
        if x == b:
            return maxC
        if dist[x][0] < maxC:
            continue
        elif dist[x][0] == maxC and dist[x][1] > totalC:
            continue
        for nx, nc in graph[x]:
            tmaxC = max(maxC, nc)
            ttotalC = totalC + nc
            if dist[nx][0] > tmaxC and ttotalC <= c:
                dist[nx][0] = tmaxC
                dist[nx][1] = ttotalC
                heapq.heappush(q, [dist[nx][0], dist[nx][1], nx])

    return -1

print(solution())
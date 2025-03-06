import heapq
INF = 10 ** 8

def dijkstra(n, sx):
    q = [[0, sx]]
    
    while q:
        d, x = heapq.heappop(q)
        if dist[sx][x] < d:
            continue
        for nx, nd in graph[x]:
            if dist[sx][nx] > d + nd:
                dist[sx][nx] = d + nd
                dist[nx][sx] = d + nd
                heapq.heappush(q, [dist[nx][sx], nx])

def solution(n, s, a, b, fares):
    global dist, graph
    answer = INF
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])
        
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    dijkstra(n, s)
    dijkstra(n, a)
    dijkstra(n, b)

    for i in range(1, n + 1):
        tmpAnswer = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, tmpAnswer)

    return answer
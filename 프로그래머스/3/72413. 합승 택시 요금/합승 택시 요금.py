import heapq
INF = 10 ** 8

def floyd_warshall(n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def solution(n, s, a, b, fares):
    global dist
    answer = INF
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    for i in range(1, n + 1):
        dist[i][i] = 0
    floyd_warshall(n)

    for i in range(1, n + 1):
        tmpAnswer = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, tmpAnswer)

    return answer
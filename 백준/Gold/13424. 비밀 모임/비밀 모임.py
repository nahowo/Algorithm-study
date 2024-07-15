import sys
input = sys.stdin.readline
INF = sys.maxsize

def floydWarshall():
    for k in range(1, n + 1):
        dist[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def solution():
    global n, dist
    n, m = map(int, input().split())
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = c
        dist[b][a] = c

    k = int(input())
    friends = list(map(int, input().split()))
    floydWarshall()

    minDist = INF
    argMin = 0
    for i in range(1, n + 1):
        tmpDist = 0
        for j in range(k):
            tmpDist += dist[i][friends[j]]
        if tmpDist < minDist:
            minDist = tmpDist
            argMin = i

    return argMin

t = int(input())
for _ in range(t):
    print(solution())
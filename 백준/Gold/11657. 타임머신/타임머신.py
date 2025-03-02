import sys
input = sys.stdin.readline
INF = 10 ** 8

def solution():
    n, m = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(m)]
    dist = [INF] * (n + 1)
    dist[1] = 0

    for i in range(n):
        updated = False # 완화 여부
        for a, b, c in route:
            if dist[a] != INF and dist[b] > dist[a] + c:
                updated = True
                dist[b] = dist[a] + c
    if updated: # n번째 완화에서 완화가 이루어졌다면 음수 사이클 존재
        print(-1)
        return
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
    return

solution()
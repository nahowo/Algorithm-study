import sys
input = sys.stdin.readline
INF = 10 ** 8

def solution():
    n, m, w = map(int, input().split())
    route = []
    # 도로는 무방향 자연수 그래프, 웜홀은 방향 음수 그래프
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        route.append([a, b, c])
        route.append([b, a, c])
    for i in range(w):
        a, b, c = list(map(int, input().split()))
        route.append([a, b, -c])
    # 전체 그래프에서 음수 사이클이 하나라도 존재하는지 판별
    dist = [INF] * (n + 1)
    dist[1] = 0
    for i in range(n):
        updated = False
        for a, b, c in route:
            if dist[b] > dist[a] + c:
                updated = True
                dist[b] = dist[a] + c
    if updated:
        return "YES"
    return "NO"

tc = int(input())
for _ in range(tc):
    print(solution())
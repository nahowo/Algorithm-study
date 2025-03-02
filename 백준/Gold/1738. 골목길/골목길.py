import sys
input = sys.stdin.readline
INF = 10 ** 8

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w  = list(map(int, input().split()))
        graph[u].append([v, w])
    parent = [0] * (n + 1)
    # 양수 사이클 / 시작지 -> 도착지 경로 존재 여부를 벨만-포드로 판별
    dist = [-INF] * (n + 1)
    dist[1] = 0
    for i in range(n):
        for u in range(1, n + 1):
            for v, w in graph[u]:
                if dist[u] != -INF and dist[v] < dist[u] + w:
                    parent[v] = u
                    dist[v] = dist[u] + w
                    if i == n - 1: # 마지막 단계에서 완화가 이루어지는 경우 1 -> u 사이에는 사이클 존재, u != n일 수도 있음
                        dist[v] = INF
    
    if dist[n] == INF:
        return '-1'

    answer = []
    while n != 0:
        answer.append(n)
        n = parent[n]
    
    return ' '.join(map(str, answer[::-1]))

print(solution())
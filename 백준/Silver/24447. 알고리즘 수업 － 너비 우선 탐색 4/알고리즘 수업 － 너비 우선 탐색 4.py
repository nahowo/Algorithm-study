import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        graph[i].sort()
    dist = [-1] * (n + 1)
    time = [0] * (n + 1)
    cnt = 1

    dist[r] = 0
    time[r] = 1
    q = deque([r])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == -1:
                cnt += 1
                dist[nx] = dist[x] + 1
                time[nx] = cnt
                q.append(nx)

    answer = 0
    for i in range(1, n + 1):
        answer += dist[i] * time[i]
    return answer

print(solution())
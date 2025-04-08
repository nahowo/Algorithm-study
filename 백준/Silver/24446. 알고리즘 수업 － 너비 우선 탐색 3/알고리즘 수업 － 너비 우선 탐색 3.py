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

    dist = [-1] * (n + 1)
    dist[r] = 0
    q = deque([r])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
                
    return '\n'.join(map(str, dist[1:]))

print(solution())
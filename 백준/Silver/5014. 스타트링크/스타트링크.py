import sys
from collections import deque
input = sys.stdin.readline
INF = 10 ** 7

def solution():
    f, s, g, u, d = map(int, input().split())
    
    dist = [INF] * (f + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        if x == g:
            return dist[x]
        for nx in [x + u, x - d]:
            if 0 < nx <= f:
                if dist[nx] == INF:
                    dist[nx] = dist[x] + 1
                    q.append(nx)

    return "use the stairs"

print(solution())
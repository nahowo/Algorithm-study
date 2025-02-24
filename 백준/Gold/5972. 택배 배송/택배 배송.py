import sys
import heapq
input = sys.stdin.readline
MAX_SIZE = 10 ** 9

def solution():
    n, m = map(int, input().split())
    road = [dict() for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if b in road[a]:
            road[a][b] = min(road[a][b], c)
        else:
            road[a][b] = c
        if a in road[b]:
            road[b][a] = min(road[b][a], c)
        else:
            road[b][a] = c
    visited = [False] * (n + 1)
    cnt = [MAX_SIZE] * (n + 1)
    cnt[1] = 0
    q = [[cnt[1], 1]]

    while q:
        dist, x = heapq.heappop(q)
        if visited[x]:
            continue
        for nx, c in road[x].items():
            if not visited[nx]:
                cnt[nx] = min(cnt[nx], cnt[x] + c)
                heapq.heappush(q, [cnt[nx], nx])
        visited[x] = True

    return cnt[n]

print(solution())
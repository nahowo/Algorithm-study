import sys
import heapq
input = sys.stdin.readline
MAX_SIZE = 10 ** 6

def solution():
    answer = []
    n, m, k, sx = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    visited = [False] * (n + 1)
    cnt = [MAX_SIZE] * (n + 1)
    cnt[sx] = 0
    q = [[cnt[sx], sx]]

    while q:
        dist, x = heapq.heappop(q)
        if visited[x]:
            continue
        for nx in graph[x]:
            if not visited[nx]:
                cnt[nx] = min(cnt[nx], cnt[x] + 1)
                heapq.heappush(q, [cnt[nx], nx])
        visited[x] = True
        if cnt[x] == k:
            answer.append(x)

    answer.sort()
    if len(answer) == 0:
        print(-1)
    for i in answer:
        print(i)

solution()
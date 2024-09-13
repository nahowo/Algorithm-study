import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    idg = [0 for _ in range(n + 1)] # 진입 간선
    dp = [0 for _ in range(n + 1)] # i번째 건물을 짓기 위한 최소 시간

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        idg[y] += 1
    
    w = int(input())

    q = deque()
    for i in range(1, n + 1):
        if idg[i] == 0:
            q.append(i)
            dp[i] = d[i]
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            idg[nx] -= 1
            dp[nx] = max(dp[nx], dp[x] + d[nx])
            if idg[nx] == 0:
                q.append(nx)

    return dp[w]

t = int(input())
for _ in range(t):
    print(solution())
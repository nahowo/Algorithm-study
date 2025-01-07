import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, c, sx):
    cnt = 1
    totalCandy = c[sx]
    q = deque()
    q.append(sx)
    visited[sx] = True

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                totalCandy += c[nx]
                q.append(nx)
    return [cnt, totalCandy]

def solution():
    global n, visited
    n, m, k = map(int, input().split())
    c = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    candy = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            candy.append(bfs(graph, c, i))

    dp = [[-1] * k for _ in range(len(candy) + 1)]
    for i in range(1, len(candy) + 1):
        dp[i - 1][0] = 0
        cnt, totalCnt = candy[i - 1]
        for j in range(k):
            if dp[i - 1][j] > -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j + cnt < k:
                    dp[i][j + cnt] = max(dp[i][j + cnt], dp[i - 1][j] + totalCnt)

    return max(dp[-1])
    
print(solution())
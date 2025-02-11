import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, sx):
    q = deque()
    visited = [False] * (n + 1)
    visited[sx] = True
    q.append(sx)
    cnt = 0

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                cnt += 1
    return cnt

def solution():
    global n
    n, m = map(int, input().split())
    answer = 0
    big = [[] for _ in range(n) for _ in range(n + 1)] # 본인보다 무거운 구슬
    small = [[] for _ in range(n) for _ in range(n + 1)] # 본인보다 가벼운 구슬
    for _ in range(m):
        a, b = map(int, input().split())
        small[a].append(b)
        big[b].append(a)
    
    for i in range(1, n + 1):
        if bfs(big, i) > (n - 1) // 2 or bfs(small, i) > (n - 1) // 2:
            answer += 1
    return answer
    
print(solution())
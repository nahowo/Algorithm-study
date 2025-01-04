import sys
from collections import deque
input = sys.stdin.readline

def checkColor(graph, color):
    visited = [False] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    cnt = 0 if color[1] == 0 else 1
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                if color[x] != color[nx]:
                    cnt += 1
                visited[nx] = True
                q.append(nx)
    return cnt

def solution():
    global n
    n = int(input())
    color = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)] # 연결 정보
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    return checkColor(graph, color)

print(solution())
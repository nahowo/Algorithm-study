import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph):
    visited = [-1] * (n + 1)
    visited[start] = 0
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
    return visited

def solution():
    global n
    n, s, p = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    nodeDist = []
    visited = bfs(p, graph)
    for i in range(1, s + 1):
        nodeDist.append(visited[i])
    
    nodeDist.sort()
    return n - (nodeDist[0] + nodeDist[1]) - 1

print(solution())
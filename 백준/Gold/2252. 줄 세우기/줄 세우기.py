import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(x, graph):
    global cnt
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx, graph)
    result[cnt] = x
    cnt -= 1

def solution():
    global visited, result, cnt
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    visited = [False] * (n + 1)
    result = [0] * (n)
    cnt = n - 1
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph)
    
    return result

print(*solution())
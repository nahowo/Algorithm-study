import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

def dfs(x):
    for nx in connect[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx)
            size[x] += size[nx]

def solution():
    global connect, size, visited
    n, r, q = map(int, input().split())
    connect = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        connect[u].append(v)
        connect[v].append(u)

    size = [1] * (n + 1)
    visited = [False] * (n + 1)
    visited[r] = True
    dfs(r)

    for _ in range(q):
        u = int(input())
        print(size[u])

solution()
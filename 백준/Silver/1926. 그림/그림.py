import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    visited[i][j] = True
    q = deque([[i, j]])
    size = 1
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and painting[ni][nj] == "1" and not visited[ni][nj]:
                size += 1
                visited[ni][nj] = True
                q.append([ni, nj])
    return size

def solution():
    global n, m, painting, visited
    n, m = map(int, input().split())
    painting = [input().rstrip().split(" ") for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    answer = [0, 0]
    
    for i in range(n):
        for j in range(m):
            if painting[i][j] == "1" and not visited[i][j]:
                answer[0] += 1
                size = bfs(i, j)
                answer[1] = max(answer[1], size)
    
    return '\n'.join(map(str, answer))
    
print(solution())
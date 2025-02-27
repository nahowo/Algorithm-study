import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(h):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for si in range(n):
        for sj in range(n):
            if not visited[si][sj]:
                if maps[si][sj] <= h:
                    visited[si][sj] = True
                    continue
                q = deque()
                q.append([si, sj])
                visited[si][sj] = False
                while q:
                    i, j = q.popleft()
                    for di, dj in d:
                        ni, nj = i + di, j +dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and maps[ni][nj] > h:
                            visited[ni][nj] = True
                            q.append([ni, nj])
                cnt += 1
    return cnt

def solution():
    global maps, n
    n = int(input())
    maps = []
    heights = {0}
    for _ in range(n):
        tmp = list(map(int, input().split()))
        maps.append(tmp)
        heights.update(tmp)

    answer = 0
    for i in heights:
        answer = max(answer, bfs(i))
    return answer

print(solution())
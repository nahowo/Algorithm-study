import sys
import heapq
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
MAX_SIZE = 10 ** 5

def solution(n):
    cave = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    cnt = [[MAX_SIZE] * n for _ in range(n)]
    cnt[0][0] = cave[0][0]
    q = [[cnt[0][0], 0, 0]]

    while q:
        dist, x, y = heapq.heappop(q)
        if visited[x][y]:
            continue
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                cnt[nx][ny] = min(cnt[nx][ny], cnt[x][y] + cave[nx][ny])
                heapq.heappush(q, [cnt[nx][ny], nx, ny])
        visited[x][y] = True

    return cnt[n - 1][n - 1]

idx = 1
while 1:
    n = int(input())
    if n == 0:
        break
    print("Problem " + str(idx) + ": " + str(solution(n)))
    idx += 1
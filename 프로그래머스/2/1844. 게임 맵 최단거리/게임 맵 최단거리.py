from collections import deque
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    cnt = [[-1] * (m) for _ in range(n)]
    cnt[0][0] = 1
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if cnt[nx][ny] == -1:
                    cnt[nx][ny] = cnt[x][y] + 1
                    q.append([nx, ny])

    answer = cnt[n - 1][m - 1]
    
    return answer
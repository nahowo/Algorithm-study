import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    m, n, k = map(int, input().split())
    paper = [[0] * n for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                paper[i][j] = 1
    
    count = 0
    sizeArr = []
    for si in range(m):
        for sj in range(n):
            if paper[si][sj] == 0:
                paper[si][sj] = 1
                q = deque()
                q.append([si, sj])
                size = 1
                while q:
                    i, j = q.popleft()
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and paper[ni][nj] == 0:
                            paper[ni][nj] = 1
                            q.append([ni, nj])
                            size += 1
                count += 1
                sizeArr.append(size)
    print(count)
    print(*sorted(sizeArr))

solution()
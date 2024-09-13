import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(red, blue):
    q = deque()
    q.append((red[0], red[1], blue[0], blue[1]))
    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))
    cnt = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10:
                return -1

            if board[rx][ry] == 'O':
                return cnt

            for dx, dy in d:
                nrx, nry = move(dx, dy, rx, ry, 'R')
                nbx, nby = move(dx, dy, bx, by, 'B')
                if nbx == 'F' and nby == 'F':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1
    
def move(dx, dy, x, y, type):
    while True:
        x += dx
        y += dy
        if board[x][y] == '#':
            x -= dx
            y -= dy
            return x, y
        elif board[x][y] == 'O':
            if type == 'R':
                return x, y
            else:
                return 'F', 'F'

n, m = map(int, input().split())
board = []
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == 'R':
            red = [i, j]
        elif tmp[j] == 'B':
            blue = [i, j]
        elif tmp[j] == 'O':
            hole = (i, j)
    board.append(tmp)

print(bfs(red, blue))
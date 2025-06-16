import sys
from collections import deque
input = sys.stdin.readline
direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def solution():
    n, m = map(int, input().split())
    board = [[-1] * n for _ in range(n)]
    answer = [''] * m
    move = [[0] * n for _ in range(n)]
    x, y = map(int, input().split())
    q = deque([])
    q.append([x - 1, y - 1])

    for i in range(m):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = i
    
    while q:
        if m == 0:
            break
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -2:
                move[nx][ny] = move[x][y] + 1
                q.append([nx, ny])
                if board[nx][ny] != -1:
                    m -= 1
                    answer[board[nx][ny]] = str(move[nx][ny])
                board[nx][ny] = -2
    return ' '.join(answer)

print(solution())
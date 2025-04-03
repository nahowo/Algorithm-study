import sys
from collections import deque
input = sys.stdin.readline
direction = {1: [1, 2, 4], 2: [2, 1, 3, 5], 3: [3, 2, 6], 4: [4, 1, 5, 7], 5: [5, 2, 4, 6, 8], 6: [6, 3, 5, 9], 7: [7, 4, 8], 8: [8, 5, 7, 9], 9: [9, 6, 8]}

def toBit(board):
    b = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                b += 1 << ((3 - i - 1) * 3 + (3 - j - 1))
    return b

def click(x, pos):
    b = 0
    for t in direction[pos]:
        b += 1 << (t - 1)
    return x ^ b

def solution():
    board = [input().rstrip() for _ in range(3)]
    goal = toBit(board)
    
    cnt = dict()
    cnt[0] = 0
    q = deque([0])

    while q:
        x = q.popleft()
        if x == goal:
            return cnt[x]
        for i in range(1, 10):
            nx = click(x, i)
            if nx not in cnt:
                cnt[nx] = cnt[x] + 1
                q.append(nx)

p = int(input())
for _ in range(p):
    print(solution())
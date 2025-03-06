from copy import deepcopy
from itertools import product
direction = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

def rotate(i, j, t):
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            clock[ni][nj] = (clock[ni][nj] + t) % 4

def solution(clockHands):
    global n, clock
    answer = 10 ** 4
    n = len(clockHands)
    
    for c in product(range(4), repeat = n):
        clock = deepcopy(clockHands)
        for j in range(n):
            rotate(0, j, c[j])
        cnt = sum(c)
        
        for i in range(n - 1):
            for j in range(n):
                if clock[i][j] != 0:
                    turn = 4 - clock[i][j]
                    rotate(i + 1, j, turn)
                    cnt += turn
        if sum(clock[n - 1]) == 0:
            answer = min(answer, cnt)
        
    return answer
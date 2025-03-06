import sys
from itertools import product
from copy import deepcopy
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
INF = 10 ** 8

def click(i, j):
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < 10 and 0 <= nj < 10:
            tLight[ni][nj] = not tLight[ni][nj]

def solution():
    global tLight
    answer = INF
    light = [[True] * 10 for _ in range(10)]
    for i in range(10):
        tmp = input().rstrip()
        for j in range(10):
            if tmp[j] == '#':
                light[i][j] = False

    for c in product((True, False), repeat = 10): # c는 해당 인덱스를 돌리는지 여부
        # 첫번째 줄 바꾸기
        tLight = deepcopy(light)
        for j in range(10):
            if c[j]:
                click(0, j)
        cnt = sum(c)

        # 두번째 줄 이상부터 바꾸기
        for i in range(9):
            for j in range(10):
                if tLight[i][j]:
                    click(i + 1, j)
                    cnt += 1
        
        # 마지막 줄을 바꿀 수 있는지 확인
        if sum(tLight[9]) == 0:
            answer = min(answer, cnt)

    return answer

print(solution())
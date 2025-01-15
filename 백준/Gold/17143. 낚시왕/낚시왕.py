import sys
input = sys.stdin.readline

shift = lambda x: -1 * x

def catchShark(pos):
    size = 0
    for i in range(r):
        if board[i][pos]:
            size = shark[board[i][pos]][4]
            del shark[board[i][pos]]
            board[i][pos] = 0
            break
    return size

def moveShark(s, d, rc, pos): # s: 속도, d: 방향, rc: 가로면 r, 세로면 c 크기
    s = s % (rc * 2 - 2)
    dr = 1 if 2 <= d <= 3 else -1

    for _ in range(s):
        if pos + dr < 0:
            pos = 1
            dr = shift(dr)
        elif pos + dr > rc - 1:
            pos = rc - 2
            dr = shift(dr)
        else:
            pos += dr
    if 1 <= d <= 2: # 상하
        if dr == -1:
            d = 1
        else:
            d = 2
    else: # 좌우
        if dr == -1:
            d = 4
        else:
            d = 3
    return d, pos

def solution():
    global r, c, shark, board
    r, c, m = map(int, input().split())
    shark = dict()
    board = [[0] * (c) for _ in range(r)]
    for i in range(65, m + 65):
        shark[chr(i)] = list(map(int, input().split()))
        shark[chr(i)][0] -= 1
        shark[chr(i)][1] -= 1
        board[shark[chr(i)][0]][shark[chr(i)][1]] = chr(i)
    
    result = 0
    for i in range(c):
        # 1. 이동 후 상어 낚시
        result += catchShark(i)

        # 2. 상어 이동
        eaten = []
        tmpBoard = [[0] * (c) for _ in range(r)]
        for id, tmp in shark.items():
            tr, tc, ts, td, tz = tmp
            if 1 <= td <= 2:
                dr, tr = moveShark(ts, td, r, tr)
                shark[id][0] = tr
                shark[id][3] = dr
            else:
                dr, tc = moveShark(ts, td, c, tc)
                shark[id][1] = tc
                shark[id][3] = dr

            if tmpBoard[tr][tc]:
                if shark[tmpBoard[tr][tc]][4] < tz: # 교체 가능한 경우
                    eaten.append(tmpBoard[tr][tc])
                    tmpBoard[tr][tc] = id
                else:
                    eaten.append(id)
            else:
                tmpBoard[tr][tc] = id
        board = tmpBoard.copy()
        for es in eaten:
            del shark[es]
    
    return result
    
print(solution())
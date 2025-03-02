import sys
input = sys.stdin.readline
d = [0, (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def calcDist(tx, ty, x, y):
    rx, ry = 0, 0
    dist = 200
    for dx, dy in d[1:]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            tmpDist = abs(tx - nx) + abs(ty - ny)
            if tmpDist < dist:
                dist = tmpDist
                rx, ry = nx, ny
    return rx, ry

def checkOver(jx, jy, arduinos):
    for ax, ay in arduinos.values():
        if ax == jx and ay == jy:
            return True
    return False

def solution():
    global board, r, c
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    cmd = input().rstrip()
    arduinos = dict()
    idx = 0
    jx, jy = 0, 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                board[i][j] = '.'
                arduinos[idx] = [i, j]
                idx += 1
            elif board[i][j] == 'I':
                jx, jy = i, j

    for i in range(len(cmd)):
        # 종수 이동
        board[jx][jy] = '.'
        jx += d[int(cmd[i])][0]
        jy += d[int(cmd[i])][1]
        board[jx][jy] = 'I'
        # 미친 아두이노 이동
        visited = [[-1] * c for _ in range(r)]
        boom = set()
        for j in arduinos.keys():
            ax, ay = arduinos[j]
            nax, nay = calcDist(jx, jy, ax, ay)
            arduinos[j] = [nax, nay]
            if visited[nax][nay] != -1:
                boom.add(visited[nax][nay])
                boom.add(j)
            else:
                visited[nax][nay] = j
        # 종료 여부 판별
        if checkOver(jx, jy, arduinos):
            print("kraj", str(i + 1))
            return
        # 겹친 아두이노 제거
        for bidx in boom:
            del arduinos[bidx]
    for ax, ay in arduinos.values():
        board[ax][ay] = 'R'
    
    for i in range(r):
        print(''.join(board[i]))
    
solution()
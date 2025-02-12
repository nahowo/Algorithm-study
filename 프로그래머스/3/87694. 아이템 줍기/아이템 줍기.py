from collections import deque
D = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    for i in range(len(rectangle)):
        rectangle[i][0] *= 2
        rectangle[i][1] *= 2
        rectangle[i][2] *= 2
        rectangle[i][3] *= 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    cnt = [[-1] * 102 for _ in range(102)]
    cnt[characterX][characterY] = 0
    q = deque()
    q.append([characterX, characterY])
    
    while q:
        x, y = q.popleft()
        if x == itemX and y == itemY:
            break
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if cnt[nx][ny] == -1 and 0 < nx <= 100 and 0 < ny <= 100:
                flag = False
                for x1, y1, x2, y2 in rectangle:
                    # 모든 사각형의 외부(경계 포함)에 존재
                    if x1 < nx < x2 and y1 < ny < y2:
                        flag = False
                        break
                    # 적어도 하나의 경계 위에 위치해야 함
                    if (x1 <= x <= x2 and x1 <= nx <= x2 and (ny == y1 or ny == y2)) or (y1 <= y <= y2 and y1 <= ny <= y2 and (nx == x1 or nx == x2)):
                        flag = True
                if flag:
                    q.append([nx, ny])
                    cnt[nx][ny] = cnt[x][y] + 0.5
    answer = int(cnt[itemX][itemY])
                    
    return answer
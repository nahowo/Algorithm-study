from collections import deque
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(sx, sy, room):
    q = deque()
    q.append([sx, sy])
    check = [[-1] * 5 for _ in range(5)]
    check[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and check[nx][ny] == -1:
                if room[nx][ny] == 'P':
                    return False
                elif room[nx][ny] == 'O':
                    check[nx][ny] = check[x][y] + 1
                    if check[nx][ny] < 2:
                        q.append([nx, ny])

    return True

def checkRoom(room):
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                res = bfs(i, j, room)
                if not res:
                    return False
    return True

def solution(places):
    answer = []
    
    for tmp in places:
        if checkRoom(tmp):
            answer.append(1)
        else:
            answer.append(0)
                
    return answer
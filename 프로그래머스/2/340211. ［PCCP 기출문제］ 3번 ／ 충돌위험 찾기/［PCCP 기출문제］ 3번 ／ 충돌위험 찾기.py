from collections import deque

def solution(points, routes):
    def move(x1, y1, x2, y2):
        if x1 > x2:
            return x1 - 1, y1
        elif x1 < x2:
            return x1 + 1, y1
        else:
            if y1 > y2:
                return x1, y1 - 1
            elif y1 < y2:
                return x1, y1 + 1
            else:
                return x2, y2
    
    def checkCrash(posD, n):
        crashCnt = 0
        board = [[0] * (101) for _ in range(101)]
        for x, y in posD.values():
            board[x][y] += 1
        for i in range(101):
            for j in range(101):
                if board[i][j] > 1:
                    crashCnt += 1
        return crashCnt

    # 전처리
    n = len(points)
    answer = 0
    coordinate = dict()
    for i in range(1, len(points) + 1):
        coordinate[i] = points[i - 1]
    robots = dict()
    pos = dict()
    for i in range(len(routes)):
        robots[i] = deque()
        pos[i] = coordinate[routes[i][0]]
        for j in routes[i][1:]:
            robots[i].append(coordinate[j])

    done = [False] * (len(robots))
    cnt = {i for i in range(len(robots.keys()))}

    answer += checkCrash(pos, n)

    while cnt:
        # 로봇 이동
        for i in cnt:
            x, y = pos[i]
            dx, dy = robots[i][0]
            nx, ny = move(x, y, dx, dy)
            pos[i] = [nx, ny]

        # 충돌 확인
        answer += checkCrash(pos, n)
        
        # 다음 도착지 설정
        for i in cnt.copy():
            if pos[i] == robots[i][0]:
                robots[i].popleft()
            if len(robots[i]) == 0:
                del pos[i]
                cnt.remove(i)

    return answer
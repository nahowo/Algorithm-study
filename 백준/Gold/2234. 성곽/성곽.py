import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def solution():
    global n, m, m
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(m)]
    roomNumber = [[0] * n for _ in range(m)]
    canMeet = dict()
    
    rooms = dict()
    roomSize = dict()
    cnt = 1
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                rooms[cnt] = {(i, j)}
                roomNumber[i][j] = cnt
                canMeet[cnt] = set()

                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx, ny = x + direction[idx][0], y + direction[idx][1]
                        if 0 <= nx < m and 0 <= ny < n:
                            if (1 << idx) & maps[x][y] == 0 and not visited[nx][ny]: # 이동 가능하다면
                                visited[nx][ny] = True
                                rooms[cnt].add((nx, ny))
                                roomNumber[nx][ny] = cnt
                                q.append([nx, ny])
                            else: # 이동 불가능하다면(경계라면)
                                if roomNumber[nx][ny] != 0 and roomNumber[nx][ny] != cnt:
                                    canMeet[cnt].add(roomNumber[nx][ny])
                                    canMeet[roomNumber[nx][ny]].add(cnt)

                roomSize[cnt] = len(rooms[cnt])
                cnt += 1
    answer1 = len(rooms)
    answer2 = max(roomSize.values())
    answer3 = 0
    for x, nxList in canMeet.items():
        for nx in nxList:
            answer3 = max(answer3, roomSize[x] + roomSize[nx])

    print(answer1)
    print(answer2)
    print(answer3)

solution()
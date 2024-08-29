import sys
from collections import deque
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def setVisited():
    return [[False] * (w) for _ in range(h)]

def bfs(sx, sy):
    global paper
    q = deque()
    q.append([sx, sy])
    visited = setVisited()
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and MAP[nx][ny] != "*":
                p = MAP[nx][ny]
                if 65 <= ord(p) <= 90: # 문을 발견한 경우
                    if p.lower() not in keys: # 열 수 없는 문인 경우
                        continue
                elif 97 <= ord(p) <= 122 and p not in keys: # 새 열쇠를 발견한 경우
                    visited = setVisited()
                    keys.add(p)
                elif p == "$": # 문서를 발견한 경우
                    paper += 1
                MAP[nx][ny] = '.'
                visited[nx][ny] = True
                q.append([nx, ny])
    return

def solution():
    global h, w, MAP, keys, paper
    h, w = map(int, input().split())
    h += 2 # 건물 출입을 위한 패딩 적용
    w += 2
    MAP = [['.'] * (w)]

    paper = 0
    for _ in range(h - 2):
        MAP.append(['.'] + list(input().rstrip()) + ['.'])
    MAP.append(['.'] * (w))
    keys = set(list(input().rstrip()))
    
    bfs(0, 0)
    
    return paper

t = int(input())
for _ in range(t):
    print(solution())
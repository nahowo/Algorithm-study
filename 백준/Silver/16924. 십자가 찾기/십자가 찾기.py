import sys
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def checkCross(x, y):
    size = 1
    toCheck = [[x, y]]
    while True:
        tmpCheck = []
        for dx, dy in direction:
            nx, ny = x + dx * size, y + dy * size
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '*':
                tmpCheck.append([nx, ny])
        if len(tmpCheck) == 4:
            toCheck.extend(tmpCheck)
            size += 1
        else:
            if size > 1:
                for tx, ty in toCheck:
                    visited[tx][ty] = 0
            return size - 1
    
def solution():
    global n, m, grid, visited
    n, m = map(int, input().split())
    grid = [input().rstrip() for _ in range(n)]
    visited = [[0] * (m) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                visited[i][j] = 1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                ret = checkCross(i, j)
                for k in range(1, ret + 1):
                    answer.append(str(i + 1) + ' ' + str(j + 1) + ' ' + str(k))

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                return -1
    
    print(len(answer))
    return '\n'.join(answer)

print(solution())
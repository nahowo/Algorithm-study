import sys
input = sys.stdin.readline

def recursion(n, sx, ex, sy, ey):
    if n == 2:
        tmp = []
        for x in [sx, ex]:
            for y in [sy, ey]:
                tmp.append(grid[x][y])
        tmp.sort()
        return tmp[1]

    arr = []
    for i in range(sx, ex, n // 2):
        for j in range(sy, ey, n // 2):
            second = recursion(n // 2, i, i + (n // 2) - 1, j, j + (n // 2) - 1)
            arr.append(second)
    arr.sort()
    return arr[1]

def solution():
    global grid
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    if n == 1:
        return grid[0][0]
    
    answer = recursion(n, 0, n - 1, 0, n - 1)
    return answer

print(solution())
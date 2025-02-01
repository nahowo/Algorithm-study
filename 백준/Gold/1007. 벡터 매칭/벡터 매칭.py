import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 7

def getVectorSum(posX, posY):
    x = totalX - posX * 2
    y = totalY - posY * 2
    return (x ** 2 + y ** 2) ** (1 / 2)

def bruteForce(cnt, visited, start, x, y):
    global minVectorSum
    if cnt == n // 2:
        return getVectorSum(x, y)
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            tmpVectorSum = bruteForce(cnt + 1, visited, i + 1, x + dot[i][0], y + dot[i][1])
            minVectorSum = min(minVectorSum, tmpVectorSum)
            visited[i] = False
    return minVectorSum

def solution():
    global n, dot, minVectorSum, totalX, totalY
    n = int(input())
    dot = [list(map(int, input().split())) for _ in range(n)]
    minVectorSum = INF
    visited = [False] * n
    totalX = totalY = 0
    for i in range(n):
        totalX += dot[i][0]
        totalY += dot[i][1]
    bruteForce(0, visited, 0, 0, 0)
    return minVectorSum

t = int(input())
for i in range(t):
    print(solution())
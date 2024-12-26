import sys
input = sys.stdin.readline

def findRoot(n):
    if root[n] != n:
        root[n] = findRoot(root[n])
    return root[n]

def unionRoot(a, b):
    aRoot = findRoot(a)
    bRoot = findRoot(b)
    if aRoot < bRoot:
        root[bRoot] = aRoot
    else:
        root[aRoot] = bRoot

def solution():
    global root
    n, m = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(m)]
    road.sort(key = lambda x: x[2])
    root = [i for i in range(n + 1)]
    totalCost = 0
    lastCost = 0

    for a, b, c in road:
        if findRoot(a) != findRoot(b):
            unionRoot(a, b)
            totalCost += c
            lastCost = c
    return totalCost - lastCost
    
print(solution())
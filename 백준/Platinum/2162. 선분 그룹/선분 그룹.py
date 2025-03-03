import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def ccw(x1, y1, x2, y2, x3, y3):
    s = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if s > 0:
        return 1
    elif s == 0:
        return 0
    else:
        return -1

def canMeet(x1, y1, x2, y2, x3, y3, x4, y4):
    f1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    f2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if not f1 and not f2:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
            return 1
        else:
            return 0
    else:
        if f1 <= 0 and f2 <= 0:
            return 1
        else:
            return 0

def solution():
    global parent
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            if canMeet(x1, y1, x2, y2, x3, y3, x4, y4):
                if parent[i] != parent[j]:
                    union(i, j)
    for i in range(n):
        parent[i] = find(parent[i])
    count = dict()
    for i in range(n):
        count[parent[i]] = count.get(parent[i], 0) + 1
    print(len(count))
    print(max(count.values()))

solution()
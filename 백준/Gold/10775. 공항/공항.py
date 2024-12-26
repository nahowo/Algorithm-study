import sys
input = sys.stdin.readline

def findRoot(x):
    if root[x] != x:
        root[x] = findRoot(root[x])
    return root[x]

def unionRoot(a, b):
    aRoot = findRoot(a)
    bRoot = findRoot(b)

    if a < b:
        root[bRoot] = aRoot
    else:
        root[aRoot] = bRoot

def solution():
    global root
    g = int(input())
    p = int(input())
    airplane = []
    for _ in range(p):
        airplane.append(int(input()))
    root = [i for i in range(g + 1)]
    cnt = 0

    for i in range(p):
        ap = airplane[i]
        apRoot = findRoot(ap)
        if apRoot == 0:
            break

        unionRoot(apRoot, apRoot - 1)
        cnt += 1
    return cnt
    
print(solution())
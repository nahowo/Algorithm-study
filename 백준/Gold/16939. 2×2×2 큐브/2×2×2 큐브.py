import sys
input = sys.stdin.readline

def check(cube):
    for i in range(6):
        flag = cube[4 * i + 1]
        for j in range(4 * i + 2, 4 * (i + 1) + 1):
            if cube[j] != flag:
                return False
    return True

def move(c, a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, h1, h2):
    c[a1], c[b1], c[c1], c[d1], c[e1], c[f1], c[g1], c[h1] = c[a2], c[b2], c[c2], c[d2], c[e2], c[f2], c[g2], c[h2]
    return c

def solution():
    cube = [0] + list(map(int, input().split()))
    v1 = move(cube.copy(), 1, 5, 3, 7, 5, 9, 7, 11, 9, 22, 11, 24, 22, 1, 24, 3)
    v2 = move(cube.copy(), 2, 6, 4, 8, 6, 10, 8, 12, 10, 21, 12, 23, 21, 2, 23, 4)
    h1 = move(cube.copy(), 13, 5, 14, 6, 5, 17, 6, 18, 17, 21, 18, 22, 21, 13, 22, 14)
    h2 = move(cube.copy(), 15, 7, 16, 8, 7, 19, 8, 20, 19, 23, 20, 24, 23, 15, 24, 16)
    t1 = move(cube.copy(), 1, 15, 2, 13, 13, 11, 15, 12, 11, 20, 12, 18, 20, 2, 18, 1)
    t2 = move(cube.copy(), 1, 18, 2, 20, 18, 12, 20, 11, 12, 15, 11, 13, 15, 1, 13, 2)
    result = 0
    for i in [v1, v2, h1, h2, t1, t2]:
        if check(i):
            result = 1
            break
    return result

print(solution())
import sys
input = sys.stdin.readline

def getInfo(l, d, time):
    t = L - l
    if t == 0:
        return 0, 0
    tmp = time % (2 * t)
    if d == 0: # ->
        if tmp < t:
            d = 0
            pos = tmp
        else:
            d = 1
            pos = t - (tmp - t)
    else: # <-
        if tmp < t:
            d = 1
            pos = t - (tmp)
        else:
            d = 0
            pos = tmp - t
    return d, pos

def move(pos, d, l):
    t = L - l
    if d == 0:
        if pos == t:
            d = 1
            pos -= 1
        else:
            pos += 1
    else:
        if pos == 0:
            d = 0
            pos += 1
        else:
            pos -= 1
    return pos

def solution():
    global L
    n, L = map(int, input().split())
    stick = [0] * n # [길이, 방향]
    for i in range(n):
        stick[i] = list(map(int, input().split()))

    time = 0
    for i in range(n - 1):
        cl, cd = stick[i]
        cd, cpos = getInfo(cl, cd, time)
        nl, nd = stick[i + 1]
        nd, npos = getInfo(nl, nd, time)

        while True:
            if not (cpos + cl < npos or cpos > npos + nl):
                break
            cpos = move(cpos, cd, cl)
            npos = move(npos, nd, nl)
            time += 1
    return time

print(solution())
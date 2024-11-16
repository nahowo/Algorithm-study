def splitQuad(arr, l, sx, ex, sy, ey):
    if l == 1:
        counter[arr[sx][sy]] += 1
        return
    flag = arr[sx][sy]
    cnt = 0
    for i in range(sx, ex):
        for j in range(sy, ey):
            if arr[i][j] != flag:
                l //= 2
                splitQuad(arr, l, sx, sx + l, sy, sy + l)
                splitQuad(arr, l, sx + l, ex, sy, sy + l)
                splitQuad(arr, l, sx, sx + l, sy + l, ey)
                splitQuad(arr, l, sx + l, ex, sy + l, ey)
                return
            else:
                cnt += 1
    if cnt == l ** 2:
        counter[flag] += 1

def solution(arr):
    global counter
    length = len(arr[0])
    counter = [0, 0]
    splitQuad(arr, length, 0, length, 0, length)
    return counter
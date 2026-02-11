def getStart(w, h, park):
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                return i, j
    return 0, 0

def checkObstacle(sx, ex, sy, ey, park):
    print("co:", sx, ex, sy, ey)
    try:
        for i in range(sx, ex):
            for j in range(sy, ey):
                print("i, j:", i, j)
                if park[i][j] == "X":
                    return False
    except IndexError:
        return False
    return True

def move1(x, y, w, h, op, n, park):
    tx, ty = x, y
    print("\n", op, n)
    print("x, y:", x, y)
    if op == "N":
        tx -= n
        if checkObstacle(tx, x, y, y + 1, park):
            print("success:", tx, ty)
            return tx, ty
    elif op == "S":
        tx += n
        if checkObstacle(x + 1, tx + 1, y, y + 1, park):
            print("success:", tx, ty)
            return tx, ty
    elif op == "W":
        ty -= n
        if checkObstacle(x, x + 1, ty, y, park):
            print("success:", tx, ty)
            return tx, ty
    elif op == "E":
        ty += n
        if checkObstacle(x, x + 1, y + 1, ty + 1, park):
            print("success:", tx, ty)
            return tx, ty
    print("fail:", x, y)
    return x, y

direction = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

def move(x, y, w, h, op, n, park):
    sx, sy = x, y
    for _ in range(n):
        nx, ny = direction[op]
        tx, ty = x + nx, y + ny
        if (0 <= tx < h and 0 <= ty < w) and park[tx][ty] != "X":
            x, y = tx, ty
        else:
            return sx, sy
    return x, y

def solution(park, routes):
    answer = []
    w = len(park[0])
    h = len(park)
    x, y = getStart(w, h, park)

    for cmd in routes:
        op, n = cmd.split()
        x, y = move(x, y, w, h, op, int(n), park)

    answer = [x, y]
    
    return answer
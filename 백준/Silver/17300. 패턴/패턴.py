import sys
input = sys.stdin.readline

screen = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
location = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

def diff(s, e):
    x, y = location[s]
    ex, ey = location[e]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 9 and 0 <= ny <= 9:
            if nx == ex and ny == ey:
                return True
    return False

def middle(a, b):
    mid = (a + b) / 2
    if int(mid) != mid:
        return False
    return int(mid)

def solution():
    l = int(input())
    a = list(map(int, input().split()))
    check = [False] * 10
    
    point = a[0]
    check[a[0]] = True
    for i in range(1, l):
        nPoint = a[i]
        if check[nPoint] == True:
            return False
        if diff(point, nPoint) == False:
            mid = middle(point, nPoint)
            if mid != False:
                if check[mid] != True:
                    return False
        check[point] = True
        point = nPoint
    return True

result = solution()
if result:
    print("YES")
else:
    print("NO")
import sys
input = sys.stdin.readline

minLength = sys.maxsize
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def select(cnt):
    global minLength
    if cnt == k:
        tmpLength = [False] * n
        for i in range(n): # 대피소를 설치한 집
            if check[i] == True:
                for j in range(n): # 대피소를 설치하지 않은 집
                    if i != j and check[j] != True:
                        if tmpLength[j] == False:
                            tmpLength[j] = dist[i][j]
                        else:
                            tmpLength[j] = min(tmpLength[j], dist[i][j])
        minLength = min(minLength, max(tmpLength))
        return
        
    for i in range(n):
        if check[i] == False:
            check[i] = True
            select(cnt + 1)
            check[i] = False

def solution():
    global dist, idx, n, k, check
    n, k = map(int, input().split())
    houses = []
    idx = dict()
    for i in range(n):
        x, y = map(int, input().split())
        idx[str(x) + ',' + str(y)] = i
        houses.append([x, y])
    
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = distance(houses[i][0], houses[i][1], houses[j][0], houses[j][1])
    
    for i in range(n):
        check = [False] * n
        check[i] = True
        select(1)
        check[i] = False

    return

solution()
print(minLength)
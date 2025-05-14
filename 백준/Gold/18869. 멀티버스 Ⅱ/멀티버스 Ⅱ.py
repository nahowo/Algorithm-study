import sys, math
input = sys.stdin.readline

def solution():
    global n
    m, n = map(int, input().split())
    composition = dict()
    for _ in range(m):
        galaxy = list(map(int, input().split()))
        gc = getComposition(galaxy)
        composition[gc] = composition.get(gc, 0) + 1
    
    answer = 0
    for cnt in composition.values():
        answer += math.comb(cnt, 2)
    return answer

def getComposition(galaxy):
    tmp = sorted(list(set(galaxy)))
    orderD = dict()
    for i, v in enumerate(tmp):
        orderD[v] = i

    arr = []
    for i in range(n):
        arr.append(orderD[galaxy[i]])
    ret = tuple(arr)
    return ret

print(solution())
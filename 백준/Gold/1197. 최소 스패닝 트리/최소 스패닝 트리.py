import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def findP(x):
    if p[x] != x:
        p[x] = findP(p[x])
    return p[x]

def unionP(a, b):
    a = findP(a)
    b = findP(b)
    p[a], p[b] = min(a, b), min(a, b)

def solution():
    global p
    v, e = map(int, input().split())
    p = [i for i in range(v + 1)] # 사이클 확인을 위한 부모 노드 번호
    minC = 0
    
    edges = []
    for _ in range(e):
        edges.append(list(map(int, input().split())))
    
    edges.sort(key = lambda x: x[2])

    for i in range(e):
        edge = edges[i]

        if findP(edge[0]) != findP(edge[1]):
            unionP(edge[0], edge[1])
            minC += edge[2]
    
    return minC

print(solution())
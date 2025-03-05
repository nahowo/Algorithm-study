import sys
input = sys.stdin.readline

def getDist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    global parent
    n = int(input())
    star = [list(map(float, input().split())) for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    edge = []
    for i in range(n):
        for j in range(i + 1, n):
            dist[i][j] = dist[j][i] = getDist(star[i][0], star[i][1], star[j][0], star[j][1])
            edge.append([dist[i][j], i, j])

    edge.sort()
    parent = [i for i in range(n)]
    answer = 0
    for i in range(len(edge)):
        l, a, b = edge[i]
        if find(a) != find(b):
            answer += l
            union(a, b)
    return round(answer, 2)

print(solution())
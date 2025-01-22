import sys
import heapq
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
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
    planet = [[] for _ in range(n)]

    for i in range(n):
        planet[i] = list(map(int, input().split())) + [i]
    
    xp = sorted(planet, key = lambda x: x[0])
    yp = sorted(planet, key = lambda x: x[1])
    zp = sorted(planet, key = lambda x: x[2])

    h = []
    for i in range(n - 1):
        heapq.heappush(h, [abs(xp[i][0] - xp[i + 1][0]), xp[i][3], xp[i + 1][3]])
        heapq.heappush(h, [abs(yp[i][1] - yp[i + 1][1]), yp[i][3], yp[i + 1][3]])
        heapq.heappush(h, [abs(zp[i][2] - zp[i + 1][2]), zp[i][3], zp[i + 1][3]])
    
    parent = [i for i in range(n)]
    cnt = 0
    cost = 0
    while cnt < n - 1:
        x, a, b = heapq.heappop(h)
        if find(a) != find(b):
            union(a, b)
            cnt += 1
            cost += x
    return cost

print(solution())
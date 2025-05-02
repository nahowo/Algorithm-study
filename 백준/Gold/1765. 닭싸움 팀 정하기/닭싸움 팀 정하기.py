import sys
input = sys.stdin.readline

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
    m = int(input())
    parent = [i for i in range(n + 1)]
    enemy = {i: set() for i in range(1, n + 1)}

    for _ in range(m):
        cmd, p, q = input().rstrip().split()
        p, q = int(p), int(q)

        if cmd == "E":
            # p -> q의 원수와 친구 맺기
            for i in enemy[q]:
                union(p, i)
            # q -> p의 원수와 친구 맺기
            for i in enemy[p]:
                union(q, i)
            # p, q 서로 원수 맺기
            enemy[p].add(q)
            enemy[q].add(p)
        else:
            union(p, q)
    for i in range(1, n + 1):
        find(i)

    return len(set(parent[1:]))
    
print(solution())
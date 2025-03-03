import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
answer = {True: "YES", False: "NO"}

def find(a):
    if a != parent[a]:
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
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd:
            print(answer[find(a) == find(b)])
        else:
            union(a, b)

solution()
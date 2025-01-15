import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

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
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(i)
            return
        union(a, b)
    
    print(0)
    return

solution()
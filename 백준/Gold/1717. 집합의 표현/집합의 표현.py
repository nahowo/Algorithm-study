import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

def solution():
    global parent
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    answer = []
    
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(a, b)
        else:
            if a == b or find(a) == find(b):
                answer.append("YES")
            else:
                answer.append("NO")
    for i in answer:
        print(i)
    
solution()
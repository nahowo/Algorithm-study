import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def func():
    n=int(input())
    global node, parent
    node=[[] for _ in range(n+1)]
    for _ in range(n-1): # 연결된 노드 정보 저장
        a,b=map(int,input().split())
        node[a].append(b)
        node[b].append(a)
    parent=[False]*(n+1)
    parent[1]=True
    visit(1)
    for i in parent[2:]:
        print(i)

def visit(s):
    for nxt in node[s]:
        if not parent[nxt]:
            parent[nxt]=s
            visit(nxt)

func()
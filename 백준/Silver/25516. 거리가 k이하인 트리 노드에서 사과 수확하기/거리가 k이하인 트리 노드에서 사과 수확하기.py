import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,k=map(int,input().split())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
apple=list(map(int,input().split()))

k_tree=set([0])
total_apple=0

def func(cnt, s): # 재귀로 k거리만큼 트리 탐색
    global k_tree
    if cnt>k:
        return 0
    for i in tree[s]:
        if func(cnt+1, i)==1:
            k_tree.add(i)
    return 1
func(0, 0)

for i in k_tree:
    if apple[i]:
        total_apple+=1
print(total_apple)
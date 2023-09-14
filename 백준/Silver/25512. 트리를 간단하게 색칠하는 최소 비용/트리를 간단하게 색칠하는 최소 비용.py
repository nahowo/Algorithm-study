import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
distance=[0]*n
cost=[]
tree=[[] for _ in range(n)]
for _ in range(n-1):
    p,c=map(int,input().split())
    tree[p].append(c)
# distance[i]: 0번 노드와 i번 노드 사이의 거리
q=deque([0])
while q:
    x=q.popleft()
    for i in tree[x]:
        distance[i]=distance[x]+1
        q.append(i)
for _ in range(n):
    cost.append(list(map(int,input().split())))
# 노드 0을 white로 칠하는 경우
w_total=0
for i in range(n):
    if distance[i]%2==0:
        w_total+=cost[i][0]
    else:
        w_total+=cost[i][1]
# 노드 0을 black으로 칠하는 경우
b_total=0
for i in range(n):
    if distance[i]%2!=0:
        b_total+=cost[i][0]
    else:
        b_total+=cost[i][1]
print(min(w_total,b_total))
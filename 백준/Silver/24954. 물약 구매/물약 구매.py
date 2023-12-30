import sys
from itertools import permutations
input=sys.stdin.readline

n=int(input())
cost=list(map(int,input().split()))
sale=[[] for _ in range(n)]
order=list(permutations(range(n),n))
answer=sum(cost)

for i in range(n):
    tmp=int(input())
    for j in range(tmp):
        sale[i].append(list(map(int,input().split())))

for i in order:
    tmp_cost=cost[:]
    tmp=0
    for j in i:
        tmp+=tmp_cost[j]
        for k in sale[j]:
            tmp_cost[k[0]-1]=max(1,tmp_cost[k[0]-1]-k[1])
    answer=min(answer,tmp)

print(answer)
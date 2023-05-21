import sys
from collections import deque
n,k=map(int,input().split())
shared=list(map(int,input().split()))
team=set(map(int,input().split()))
for _ in range(k):
    mini=-100000000
    for i in team:
        for j in shared:
            if mini<i*j:
                mini=i*j
                x=i
    team.remove(x)
team=list(team)
point=set()
for i in range(len(shared)):
    for j in range(len(team)):
        point.add(shared[i]*team[j])
print(max(point))
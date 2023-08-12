import sys
from collections import deque
input=sys.stdin.readline
n,w,L=map(int,input().split())
truck=deque(list(map(int,input().split())))
on_bridge=deque([0]*w)
time=0
while on_bridge:
    time+=1
    on_bridge.popleft()
    if truck:
        if sum(on_bridge)+truck[0]<=L:
            on_bridge.append(truck.popleft())
        else:
            on_bridge.append(0)
print(time)
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
original_q=deque(list(map(int,input().split())))
side_q=deque([])
next_person=1
while True:
    if len(original_q)==0:
        if len(side_q)>0 and side_q[0]!=next_person:
            print("Sad")
        else:
            print("Nice")
        break
    if original_q[0]==next_person:
        original_q.popleft()
        next_person+=1
    elif len(side_q)!=0 and side_q[0]==next_person:
        side_q.popleft()
        next_person+=1
    else:
        side_q.appendleft(original_q.popleft())
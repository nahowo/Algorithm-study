import sys
from collections import deque
input=sys.stdin.readline

def func():
    p=input().rstrip()
    n=int(input())
    arr=input().rstrip()
    if p.count("D")>n:
        return "error"
    
    arr=deque(arr[1:-1].split(","))
    rSwitch=False
    for i in p:
        if i=="R":
            rSwitch=not rSwitch
        else:
            if rSwitch:
                arr.pop()
            else:
                arr.popleft()
    arr=list(arr)
    if rSwitch:
        return "["+",".join(arr[::-1])+"]"
    else:
        return "["+",".join(arr)+"]"
    
t = int(input())
for _ in range(t):
    print(func())
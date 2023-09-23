import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
d=deque()
for _ in range(n):
    c=input().rstrip()
    if c[:4]=="push":
        x=c.split()[1]
        d.append(x)
    elif c=="pop":
        if len(d)==0:
            print("-1")
        else:
            print(d.popleft())
    elif c=="size":
        print(len(d))
    elif c=="empty":
        if len(d)==0:
            print('1')
        else:
            print('0')
    elif c=="front":
        if len(d)==0:
            print('-1')
        else:
            print(d[0])
    elif c=="back":
        if len(d)==0:
            print('-1')
        else:
            print(d[-1])
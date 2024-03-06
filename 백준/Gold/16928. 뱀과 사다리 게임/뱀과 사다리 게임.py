import sys
from collections import deque
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    ladder=dict()
    snake=dict()
    for _ in range(n):
        x,y=map(int,input().split())
        ladder[x]=y
    for _ in range(m):
        x,y=map(int,input().split())
        snake[x]=y
    
    board=[0]*101
    q=deque([1])
    while q:
        x=q.popleft()
        if x==100:
            return board[100]
        for i in range(1,7):
            n=x+i
            if n<=100 and not board[n]:
                if n in ladder:
                    n=ladder[n]
                elif n in snake:
                    n=snake[n]
                if not board[n]:
                    board[n]=board[x]+1
                    q.append(n)

print(func())
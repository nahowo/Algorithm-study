import sys
input=sys.stdin.readline

def func():
    a,c,b,_,res=input().split()
    a=int(a)
    b=int(b)
    res=int(res)
    if c=='+':
        if a+b==res:
            return 'correct'
    elif c=='-':
        if a-b==res:
            return 'correct'
    elif c=='*':
        if a*b==res:
            return 'correct'
    else:
        if a/b==res:
            return 'correct'
    return 'wrong answer'

t=int(input())
for _ in range(t):
    print(func())
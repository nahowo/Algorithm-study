import sys
input=sys.stdin.readline

def func():
    a=input().rstrip()
    b=input().rstrip()
    c=int(input())
    print(int(a)+int(b)-c)
    print(int(a+b)-c)
func()
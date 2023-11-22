import sys
input=sys.stdin.readline

n=int(input())
def func():
    an=list(map(int,input().split()))
    a=an[1:]
    an=an[0]
    bn=list(map(int,input().split()))
    b=bn[1:]
    bn=bn[0]
    ac=[a.count(4),a.count(3),a.count(2),a.count(1)]
    bc=[b.count(4),b.count(3),b.count(2),b.count(1)]
    for i in range(4):
        if ac[i]>bc[i]:
            return 'A'
        elif ac[i]<bc[i]:
            return 'B'
    return 'D'
for _ in range(n):
    print(func())
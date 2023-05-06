import sys
input=sys.stdin.readline
t=int(input())
def func(money):
    a=[0,0,0,0] #quarter, dime, nickel, penny
    b=[25,10,5,1]
    for i in range(4):
        a[i]+=money//b[i]
        money%=b[i]
    return a
for i in range(t):
    c=int(input())
    print(*func(c))
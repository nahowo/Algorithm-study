import sys
input=sys.stdin.readline

def func():
    a,b,c=map(int,input().split())
    basic=dict()
    special=dict()
    service=dict()

    for _ in range(a):
        menu,price=input().split()
        basic[menu]=int(price)
    for _ in range(b):
        menu,price=input().split()
        special[menu]=int(price)
    for _ in range(c):
        menu=input().rstrip()
        service[menu]=int(price)
    
    n=int(input())
    totalPrice=[0,0]
    totalService=0

    for i in range(n):
        order=input().rstrip()
        if order in basic:
            totalPrice[0]+=basic[order]
        elif order in special:
            totalPrice[1]+=special[order]
        elif order in service:
            totalService+=1
    if totalPrice[1]:
        if totalPrice[0]<20000:
            return "No"
    if totalService:
        if totalService!=1:
            return "No"
        if sum(totalPrice)<50000:
            return "No"
    return "Okay"


print(func())
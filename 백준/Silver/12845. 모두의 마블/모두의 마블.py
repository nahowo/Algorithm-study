import sys
input=sys.stdin.readline

def func():
    n=int(input())
    card=list(map(int,input().split()))
    if n==1:
        return card[0]
    card.sort(reverse=True)
    gold=0
    
    for i in range(1,n):
        gold+=card[0]+card[i]
    return gold

print(func())
import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    total_mood=0
    if n==0:
        for i in range(1,m+1):
            total_mood+=i**2
        return total_mood
    h=list(map(int,input().split()))
    total_h=sum(h)+n
    dep_day=m-total_h
    n+=1
    mood=[dep_day//n]*(n)
    for i in range(dep_day%n):
        mood[i]+=1
    for i in mood:
        for j in range(1,i+1):
            total_mood+=j**2
    return total_mood

print(func())
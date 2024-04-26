import sys
input=sys.stdin.readline

def func():
    n=int(input())
    people=[i for i in range(1,n+1)]
    k=1
    place=0
    while len(people)>1:
        removed=(place-1+k**3)%n
        people.remove(people[removed])
        n-=1
        k+=1
        place=removed
    return people[0]

print(func())
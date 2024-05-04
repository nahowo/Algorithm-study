import sys
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    course=list(map(int,input().split()))
    if k==sum(course):
        return n
    for i in range(len(course)):
        k-=course[i]
        if k<0:
            return i+1
        elif k==0:
            return i+2
    
    for i in range(len(course)-1,-1,-1):
        k-=course[i]
        if k<0:
            return i+1
        elif k==0:
            return i+2

print(func())
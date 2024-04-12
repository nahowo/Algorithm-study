import sys
input=sys.stdin.readline

def func():
    j,n=map(int,input().split())
    box=[]
    for _ in range(n):
        a,b=map(int,input().split())
        box.append(a*b)
    box.sort(reverse=True)

    i=0
    while j>0:
        j-=box[i]
        i+=1
    return i
        

t=int(input())
for i in range(t):
    print(func())
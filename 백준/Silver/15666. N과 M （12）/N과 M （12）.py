import sys
input=sys.stdin.readline

def func():
    if len(arr)==m:
        if tuple(arr) not in duplication:
            print(*arr)
        duplication.add(tuple(arr))
        return
    
    for i in range(len(a)):
        if len(arr)>0 and arr[-1]>a[i]:
            continue
        arr.append(a[i])
        func()
        arr.pop()

n,m=map(int,input().split())
a=list(set(map(int,input().split())))
a.sort()
arr=[]
duplication=set()
func()
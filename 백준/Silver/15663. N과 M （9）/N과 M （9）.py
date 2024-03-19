import sys
input=sys.stdin.readline

n,m=map(int,input().split())
numlist=list(map(int,input().split()))
numlist.sort()
visited=[False]*n

def func():
    p=0
    if len(arr)==m:
        print(*arr)
        return
    
    for j in range(n):
        if not visited[j] and numlist[j]!=p:
            visited[j]=True
            arr.append(numlist[j])
            p=numlist[j]
            func()
            visited[j]=False
            arr.pop()

arr=[]
func()
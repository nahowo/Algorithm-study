import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
def dfs(s):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(s,n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)
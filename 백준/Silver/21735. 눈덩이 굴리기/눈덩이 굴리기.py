import sys
input=sys.stdin.readline

n,m=map(int,input().split())
field=[0]+list(map(int,input().split()))
answer=-1
def dfs(idx,snow,t):
    global answer
    if t>m:
        return
    if t<=m:
        answer=max(answer,snow)
    if idx<=n-1:
        dfs(idx+1, snow+field[idx+1],t+1)
    if idx<=n-2:
        dfs(idx+2,snow//2+field[idx+2],t+1)

dfs(0,1,0)
print(answer)
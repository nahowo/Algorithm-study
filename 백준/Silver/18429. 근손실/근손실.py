import sys
input=sys.stdin.readline
def dfs(l,tmp):
    global cnt#,tmp#,visited
    if l==n:
        cnt+=1
        return
    for i in range(n):
        if visited[i]==0 and tmp+kit[i]-k>=0:
            visited[i]=1
            dfs(l+1,tmp+kit[i]-k)
            visited[i]=0
    tmp=0
n,k=map(int,input().split())
kit=list(map(int,input().split()))
tmp=[0,0]
cnt=tmp=0
visited=[0]*n
dfs(0,0)
print(cnt)
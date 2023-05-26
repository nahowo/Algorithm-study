import sys
input=sys.stdin.readline
n,m=map(int,input().split())
f=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    f[a].append(b)
    f[b].append(a)
stage=[0]*(n+1)
answer=0
def dfs(t,cnt):
    global answer
    if answer<cnt:
        answer=cnt #최댓값 갱신
    if t==n:
        return
    if stage[t]==0:
        for i in range(t+1,n+1):
            if stage[i]==0 and i in f[t]:
                stage[i]=1
                stage[t]=1
                dfs(t+1,cnt+2)
                stage[t]=0
                stage[i]=0
    dfs(t+1,cnt)
dfs(1,0)
if n>answer:
    print(answer+1)
else:
    print(answer)
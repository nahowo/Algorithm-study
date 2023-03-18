import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
pf=[]
for i in range(n):
    tmp=[0]
    tmp1=0
    for j in range(m):
        tmp1+=arr[i][j]
        tmp.append(tmp1)
    pf.append(tmp)
k=int(input())
answer=[]
for _ in range(k):
    i,j,x,y=map(int,input().split())
    ans=0
    for n in range(x-1,i-2,-1):
        ans+=pf[n][y]-pf[n][j-1]
    answer.append(ans)
for i in answer:
    print(i)
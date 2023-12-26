import sys
input=sys.stdin.readline

l=int(input())
n=int(input())

wish=[]
for i in range(n):
    wish.append(list(map(int,input().split())))

tmpmax=0
for i in range(n):
    if wish[i][1]-wish[i][0]>tmpmax:
        tmpmax=wish[i][1]-wish[i][0]
        res1=i+1

cake=[0 for _ in range(l+1)]
for i in range(n):
    for j in range(1,l+1):
        if wish[i][0]<=j<=wish[i][1]:
            if cake[j]==0:
                cake[j]=i+1

tmpmax=0
res2=0
for i in range(1,n+1):
    tmp=cake.count(i)
    if tmp>tmpmax:
        tmpmax=tmp
        res2=i

print(res1)
print(res2)
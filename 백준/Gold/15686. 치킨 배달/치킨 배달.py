import sys
input=sys.stdin.readline

def check(a,b):
    global minD
    if a>len(chicken):
        return
    if b==m:
        dist=0
        for r,c in house:
            d=float('inf')
            for i in val:
                nr,nc=chicken[i]
                d=min(d,abs(nr-r)+abs(nc-c))
            dist+=d
        minD=min(minD,dist)
        return
    val.append(a)
    check(a+1,b+1)
    val.pop()
    check(a+1,b)
    

def func():
    global minD, chicken, m, house, val
    n,m=map(int,input().split())
    city=[]
    chicken=[]
    house=[]
    val=[]
    for i in range(n):
        tmp=list(map(int,input().split()))
        for j in range(n):
            if tmp[j]==1:
                house.append([i,j])
            elif tmp[j]==2:
                chicken.append([i,j])
                
    minD=float('inf')
    check(0,0)
    return minD
print(func())
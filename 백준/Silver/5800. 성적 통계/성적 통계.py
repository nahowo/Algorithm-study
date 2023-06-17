import sys
input=sys.stdin.readline
k=int(input())
a=[]
for i in range(k):
    c=list(map(int,input().split()))
    tmpmax=max(c[1:])
    tmpmin=min(c[1:])
    cnum=c[0]
    c=c[1:]
    c.sort(reverse=True)
    lg=0
    for j in range(cnum-1):
        if c[j]-c[j+1]>lg:
            lg=c[j]-c[j+1]
    a.append([tmpmax,tmpmin,lg])
for i in range(k):
    print("Class",(i+1))
    print("Max",str(a[i][0])+", Min",str(a[i][1])+", Largest gap "+str(a[i][2]))
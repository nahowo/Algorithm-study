import sys
input=sys.stdin.readline

m=int(input())
s=set()
a=set(range(1,21))

res=[]
for i in range(m):
    comm=input().rstrip()
    if comm=='all':
        s=a.copy()
        continue
    elif comm=='empty':
        s.clear()
        continue
    comm,x=comm.split()
    x=int(x)
    if comm=='add':
        s.add(x)
    elif comm=='remove':
        if x in s:
            s.remove(x)
    elif comm=='check':
        print(int(x in s))
    elif comm=='toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
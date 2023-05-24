import sys
input=sys.stdin.readline
n=int(input())
d=dict()
for i in range(n):
    book=input().rstrip()
    d[book]=d.get(book,0)+1
cnt=max(list(d.values()))
bestseller=[]
dk=list(d.keys())
dv=list(d.values())
for i in range(len(d)):
    if dv[i]==cnt:
        bestseller.append(dk[i])
bestseller.sort()
print(bestseller[0])
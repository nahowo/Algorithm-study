import sys
input=sys.stdin.readline
n=int(input())
minx=miny=10000
maxx=maxy=-10000
for _ in range(n):
    a,b=map(int,input().split())
    if a<minx:
        minx=a
    if a>maxx:
        maxx=a
    if b<miny:
        miny=b
    if b>maxy:
        maxy=b
print((maxx-minx)*(maxy-miny))
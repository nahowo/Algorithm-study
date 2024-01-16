import sys
input=sys.stdin.readline

by,bm,bd=map(int,input().split())
ty,tm,td=map(int,input().split())

if tm>bm or (tm==bm and td>=bd):
    year1=ty-by
else:
    year1=ty-by-1

year2=ty-by+1
year3=ty-by

print(year1)
print(year2)
print(year3)
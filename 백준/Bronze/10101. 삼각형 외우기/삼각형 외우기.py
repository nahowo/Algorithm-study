import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
c=int(input())
s=sum([a,b,c])
set=set([a,b,c])
if s==180:
    if len(set)==1:
        print("Equilateral")
    elif len(set)==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
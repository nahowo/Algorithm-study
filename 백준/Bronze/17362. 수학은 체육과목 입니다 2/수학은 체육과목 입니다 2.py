import sys
input=sys.stdin.readline
n=int(input())
n=n%8
if n==1:
    print(1)
elif n==2 or n==0:
    print(2)
elif n==3 or n==7:
    print(3)
elif n==4 or n==6:
    print(4)
else:
    print(5)
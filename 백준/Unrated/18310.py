import sys
input=sys.stdin.readline
n=int(input())
house=sorted(list(map(int,input().split())))
if n%2==0:
    answer=house[n//2-1]
else:
    answer=house[n//2]
print(answer)
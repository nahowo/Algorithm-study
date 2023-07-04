import sys
from itertools import combinations_with_replacement
input=sys.stdin.readline
n=int(input())
num=[1,5,10,50]
s=set()
data=combinations_with_replacement(num,n)
for i in data:
    s.add(sum(i))
print(len(s))
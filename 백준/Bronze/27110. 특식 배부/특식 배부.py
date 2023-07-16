import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
chicken=list(map(int,input().split()))
wanted=0
for i in chicken:
    wanted+=min(n,i)
print(wanted)
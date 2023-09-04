import sys
input=sys.stdin.readline
n=int(input())
d=dict()
for _ in range(n):
    x,t,c=map(int,input().split())
    d[t-x]=d.get(t-x,0)+c
print(max(d.values()))
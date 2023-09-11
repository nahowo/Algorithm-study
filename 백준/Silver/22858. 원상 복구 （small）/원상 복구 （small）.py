import sys
input=sys.stdin.readline
n,k=map(int,input().split())
s=list(map(int,input().split()))
d=list(map(int,input().split()))
new_s=[0]*n
for _ in range(k):
    new_s=([0]*n).copy()
    for i in range(n):
        new_s[d[i]-1]=s[i]
    s=new_s.copy()
print(*s)
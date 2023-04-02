import sys
input=sys.stdin.readline
n1,n2=map(int,input().split())
N1=list(map(int,input().split()))
N2=list(map(int,input().split()))
ans=sorted(N1+N2)
print(*ans)
import sys
input=sys.stdin.readline
n=int(input())
tower=list(map(int,input().split()))
push=1
for i in range(n-1):
    if tower[i]<=tower[i+1]:
        push+=1
print(push)
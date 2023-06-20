import sys
input=sys.stdin.readline
n=int(input())
sum_=0
answer=0
rope=[int(input()) for _ in range(n)]
rope.sort(reverse=True)
for i in range(1,n+1):
    if rope[i-1]*i>answer:
        answer=rope[i-1]*i
print(answer)
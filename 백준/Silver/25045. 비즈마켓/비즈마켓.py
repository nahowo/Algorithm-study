import sys
input=sys.stdin.readline

n,m=map(int,input().split())
product=list(map(int,input().split()))
payment=list(map(int,input().split()))
product.sort(reverse=True)
payment.sort()
answer=0

for i in range(min(n,m)):
    answer+=max(product[i]-payment[i],0)
print(answer)
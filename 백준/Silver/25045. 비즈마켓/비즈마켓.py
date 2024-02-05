import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    product=list(map(int,input().split()))
    payment=list(map(int,input().split()))
    product.sort(reverse=True)
    payment.sort()
    answer=0

    for i in range(min(n,m)):
        if product[i]-payment[i]<0:
            return answer
        answer+=product[i]-payment[i]
    return answer

print(func())
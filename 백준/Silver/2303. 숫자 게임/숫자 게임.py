import sys
input=sys.stdin.readline

def func():
    n=int(input())
    maxnum=0
    answer=1
    for i in range(1,n+1):
        card=list(map(int,input().split()))
        tmpmax=sum_calc(card)
        if tmpmax>=maxnum:
            maxnum=tmpmax
            answer=i
    return answer

def sum_calc(arr):
    answer=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                for k in range(len(arr)):
                    if i!=k and j!=k:
                        tmpsum=arr[i]+arr[j]+arr[k]
                        tmp=int(str(tmpsum)[-1])
                        if tmp>answer:
                            answer=tmp
    return answer

print(func())
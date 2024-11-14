import sys
input=sys.stdin.readline

def func():
    n=int(input())
    tmp=1
    answer=1
    for _ in range(2,n+1):
        tmp,answer=(answer)%10007,(tmp+answer)%10007
    return answer
print(func())
import sys
input=sys.stdin.readline
    
def func():
    n=int(input())
    doll=list(map(int,input().split()))
    d=dict()
    answer=0
    for i in doll:
        d[i]=d.get(i,0)+1
        answer=max(answer,d.get(i))

    return answer

print(func())
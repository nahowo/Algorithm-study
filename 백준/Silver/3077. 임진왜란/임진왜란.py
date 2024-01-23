import sys
input=sys.stdin.readline

def func():
    n=int(input())
    arr=list(input().rstrip().split())
    d=dict()
    for i in range(n):
        d[arr[i]]=i

    submit=list(input().rstrip().split())
    point=0
    for i in range(n-1):
        for j in range(i+1,n):
            if d.get(submit[i])<d.get(submit[j]):
                point+=1
    return str(point)+"/"+str(int(n*(n-1)*0.5))

print(func())
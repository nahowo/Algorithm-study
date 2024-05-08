import sys
input=sys.stdin.readline

def func():
    n=int(input())
    t=list(map(int,input().split()))
    t.sort()
    arr=[]

    if n%2==1:
        n-=1
        arr.append(t[n])

    for i in range(n//2):
        arr.append(t[i]+t[n-i-1])
    
    return max(arr)

print(func())
import sys
input=sys.stdin.readline

def func():
    n=int(input())
    m=int(input())
    s=input().rstrip()
    cnt=0
    p="IO"*n+"I"
    for i in range(m-(2*n)):
        if s[i:i+(2*n)+1]==p:
            cnt+=1
    i=0
    return cnt

print(func())
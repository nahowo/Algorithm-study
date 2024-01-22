import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    s=[]
    check=[]
    for _ in range(n):
        s.append(input().rstrip())
    for _ in range(m):
        check.append(input().rstrip())
    s.sort()
    check.sort()
    s_key=c_key=0
    cnt=0

    while s_key<n and c_key<m:
        if s[s_key]<check[c_key]:
            s_key+=1
        else:
            if s[s_key][:len(check[c_key])]==check[c_key]:
                cnt+=1
            c_key+=1
    return cnt

print(func())
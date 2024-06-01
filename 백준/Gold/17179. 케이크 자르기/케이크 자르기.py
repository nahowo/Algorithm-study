import sys
input=sys.stdin.readline

def binary(mid):
    cnt=tmp=0
    for i in s:
        if i-tmp>=mid:
            cnt+=1
            tmp=i
    return cnt

def func():
    for i in q:
        s,e=1,l
        answer=0

        while s<=e:
            m=(s+e)//2
            cnt=binary(m)
            if cnt>i:
                s=m+1
                answer=max(answer,m)
            else:
                e=m-1
        print(answer)
    return

n,m,l=map(int,input().split())
s=[]
for _ in range(m):
    s.append(int(input()))
s+=[l]
q=[]
for _ in range(n):
    q.append(int(input()))

func()
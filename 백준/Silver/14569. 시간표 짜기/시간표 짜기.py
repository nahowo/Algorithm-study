import sys
input=sys.stdin.readline

def func():
    n=int(input())
    k=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        k.append(tmp[1:])
    m=int(input())
    p=[]
    for _ in range(m):
        tmp=list(map(int,input().split()))
        p.append(set(tmp[1:]))

    available=[0]*m
    for i in range(m):
        for j in range(n):
            cnt=0
            for t in k[j]:
                if t in p[i]:
                    cnt+=1
            if cnt==len(k[j]):
                available[i]+=1
    
    for i in available:
        print(i)

func()
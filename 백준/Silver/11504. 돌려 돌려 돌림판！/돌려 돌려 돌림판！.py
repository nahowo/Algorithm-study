import sys
input=sys.stdin.readline
t=int(input())
answer=[]
for _ in range(t):
    n,m=map(int,input().split())
    x=int(''.join(list(map(str,input().split()))))
    y=int(''.join(list(map(str,input().split()))))
    wheel=list(map(str,input().split()))
    tmp=''.join(wheel[:m])
    cnt=0
    for i in range(1,n+1):
        if x<=int(tmp)<=y:
            cnt+=1
        tmp=tmp[1:]+wheel[(i+m-1)%n]
    answer.append(cnt)
for i in answer:
    print(i)
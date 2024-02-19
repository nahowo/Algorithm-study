import sys
input=sys.stdin.readline
    
def func():
    n=int(input())
    doll=list(map(int,input().split()))
    d=dict()
    s=set(doll)
    answer=0
    for i in doll:
        d[i]=d.get(i,0)+1
    
    while d:
        for i in s:
            if d.get(i)!=None:
                d[i]-=1
                if d[i]==0:
                    del d[i]
        answer+=1
    return answer

print(func())
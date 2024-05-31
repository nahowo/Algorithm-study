import sys
input=sys.stdin.readline

def func():
    n,k=map(int,input().split())
    t=list(map(int,input().split()))
    t.sort()
    taste=[]
    
    s=0
    e=n-1
    for i in range(k):
        if i%2==0:
            taste.append(t[e])
            e-=1
        else:
            taste.append(t[s])
            s+=1

    total_taste=taste[0]
    for i in range(len(taste)-1):
        total_taste+=max(0,taste[i+1]-taste[i])
    return total_taste

print(func())
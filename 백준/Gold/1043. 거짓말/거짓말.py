import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    truth=list(map(int,input().split()))
    truth.pop(0)
    truth=set(truth)
    party=[]

    for _ in range(m):
        people=list(map(int,input().split()))
        people.pop(0)
        party.append(set(people))

    for _ in range(m):
        for p in party:
            if p&truth: # 교집합인 경우
                truth=truth.union(p)

    cnt=m
    for p in party:
        if p&truth:
            cnt-=1
    return cnt

print(func())
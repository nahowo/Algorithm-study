import sys
input=sys.stdin.readline

def check(p,n):
    d=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
    for x,y in d:
        a1,b1=ord(p[0]),int(p[1])
        a2,b2=ord(n[0]),int(n[1])
        if a1+x==a2 and b1+y==b2:
            return True
    return False

def func():
    
    visited=set()
    answer=False
    pre=input().rstrip()
    s=pre
    for _ in range(35):
        new=input().rstrip()
        # 1. 중복 확인
        if new in visited:
            answer=True
        visited.add(new)
        # 2. 이동 가능한 위치인지 확인
        if not check(pre,new):
            answer=True
        pre=new
    if not check(pre,s): # 마지막 위치 -> 시작점 경로가 가능한지 확인
        answer=True

    if answer:
        return "Invalid"
    else:
        return "Valid"

print(func())
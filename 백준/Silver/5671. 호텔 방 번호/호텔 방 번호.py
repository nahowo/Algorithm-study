import sys
input=sys.stdin.readline

def func(n,m):
    cnt=0
    for i in range(n,m+1):
        if check(list(str(i))):
            cnt+=1
    return cnt
    
def check(arr):
    s=set()
    for i in arr:
        if i in s:
            return False
        else:
            s.add(i)
    return True

while True:
    try:
        n,m=map(int,input().split())
        print(func(n,m))
    except:
        break
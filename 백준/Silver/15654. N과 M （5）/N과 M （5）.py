import sys
input=sys.stdin.readline

n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()

def func():
    if len(arr)==m:
        print(*arr)
        return
    
    for j in range(n):
        if j!=i and j not in s:
            s.add(j)
            arr.append(num[j])
            func()
            s.remove(j)
            arr.pop()
           
for i in range(n):
    arr=[num[i]]
    s=set([i])
    func()
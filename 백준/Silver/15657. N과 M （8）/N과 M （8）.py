import sys
input=sys.stdin.readline

def func():
    global n,m,nums
    n,m=map(int,input().split())
    nums=list(map(int,input().split()))
    nums.sort()

    for i in range(n):
        s=[nums[i]]
        pick(s,i)

def pick(s,idx):
    if len(s)==m:
        print(*s)
        return
    for i in range(idx,n):
        s.append(nums[i])
        pick(s,i)
        s.pop()
    
func()
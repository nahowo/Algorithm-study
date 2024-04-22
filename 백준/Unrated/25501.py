import sys
input=sys.stdin.readline
def rec(s,l,r,count):
    if l>=r:
        return [1,count]
    elif s[l]!=s[r]:
        return [0,count]
    else:
        return rec(s,l+1,r-1,count+1)
def ispal(s):
    return rec(s,0,len(s)-1,1)
n=int(input())
answer=[]
for i in range(n):
    tmp_s=input().rstrip()
    answer.append(ispal(tmp_s))
for i in range(n):
    print(*answer[i])